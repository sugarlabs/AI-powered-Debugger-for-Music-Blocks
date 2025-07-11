import streamlit as st
import json
import pyperclip
import re
from typing import Dict, List, Set, Union, Optional


def is_base64_data(s: str) -> bool:
    """Check if string is base64 encoded data."""
    return isinstance(s, str) and bool(re.match(r'^data:(image|audio)/[a-zA-Z0-9+.-]+;base64,', s))


def get_numeric_value(block_id: Optional[str], block_map: Dict) -> Optional[Union[int, float]]:
    """Get numeric value from a block."""
    if block_id is None or block_id not in block_map:
        return None

    block = block_map[block_id]
    block_type = block[1][0] if isinstance(block[1], list) else block[1]

    if block_type == "number":
        if isinstance(block[1], list):
            return block[1][1].get('value') if isinstance(block[1][1], dict) else block[1][1]
        return block[1]
    return None


def get_text_value(block_id: Optional[str], block_map: Dict) -> Optional[str]:
    """Get text value from a block."""
    if block_id is None or block_id not in block_map:
        return None

    block = block_map[block_id]
    block_type = block[1][0] if isinstance(block[1], list) else block[1]

    if block_type == "text" and isinstance(block[1], list):
        return block[1][1].get('value')
    return None


def get_drum_name(block_id: Optional[str], block_map: Dict) -> Optional[str]:
    """Get drum name from a block."""
    if block_id is None or block_id not in block_map:
        return None

    block = block_map[block_id]
    block_type = block[1][0] if isinstance(block[1], list) else block[1]

    if block_type == "drumname" and isinstance(block[1], list):
        return block[1][1].get('value')
    return None


def get_named_box_value(block_id: Optional[str], block_map: Dict) -> Optional[str]:
    """Get named box value from a block."""
    if block_id is None or block_id not in block_map:
        return None

    block = block_map[block_id]
    block_type = block[1][0] if isinstance(block[1], list) else block[1]

    if block_type in ("namedbox", "namedarg") and isinstance(block[1], list):
        return block[1][1].get('value')
    return None


def get_block_representation(
        block_type: str,
        block_args: Optional[Dict],
        block: List,
        block_map: Dict,
        indent: int,
        is_clamp: bool,
        parent_block_type: Optional[str]
) -> Optional[str]:
    """Generate text representation for a block."""
    connections = block[-1] if isinstance(block[-1], list) else []

    try:
        if block_type == "start":
            turtle_info = [
                f"ID: {block_args.get('id', '')}",
                f"Position: ({block_args.get('xcor', 0):.2f}, {block_args.get('ycor', 0):.2f})",
                f"Heading: {block_args.get('heading', 0)}°",
                f"Color: {block_args.get('color', '')}, Shade: {block_args.get('shade', '')}",
                f"Pen Size: {block_args.get('pensize', '')}, Grey: {block_args.get('grey', 0):.2f}"
            ]
            return f"Start Block --> {{{', '.join(turtle_info)}}}"

        elif block_type == "setmasterbpm2":
            bpm_value = get_numeric_value(connections[1] if len(connections) > 1 else None, block_map)
            bpm_output = f"Set Master BPM → {bpm_value or '?'} BPM"

            if len(connections) > 2 and connections[2] in block_map and block_map[connections[2]][1] == "divide":
                divide_block = block_map[connections[2]]
                divide_connections = divide_block[-1] if isinstance(divide_block[-1], list) else []
                numerator = get_numeric_value(divide_connections[1] if len(divide_connections) > 1 else None, block_map)
                denominator = get_numeric_value(divide_connections[2] if len(divide_connections) > 2 else None,
                                                block_map)
                if numerator is not None and denominator is not None and denominator != 0:
                    bpm_output += f"\n{'│   ' * indent}├── beat value --> {numerator}/{denominator} = {(numerator / denominator):.2f}"
            return bpm_output

        elif block_type == "divide":
            numerator = get_numeric_value(connections[1] if len(connections) > 1 else None, block_map)
            denominator = get_numeric_value(connections[2] if len(connections) > 2 else None, block_map)
            result = "?"
            if numerator is not None and denominator is not None and denominator != 0:
                result = f"{(numerator / denominator):.2f}"

            if parent_block_type == "newnote":
                return f"Duration --> {numerator or '?'}/{denominator or '?'} = {result}"
            return f"Divide Block --> {numerator or '?'}/{denominator or '?'} = {result}"

        elif block_type == "storein2":
            var_name = block_args.get('value', 'unnamed')
            var_value = get_numeric_value(connections[1] if len(connections) > 1 else None, block_map)
            return f'Store Variable "{var_name}" → {var_value if var_value is not None else "?"}'

        elif block_type == "namedbox":
            return f'Variable: "{block_args.get("value", "unnamed")}"'

        elif block_type == "action":
            action_name = get_text_value(connections[1] if len(connections) > 1 else None, block_map)
            return f'Action: "{action_name or "unnamed"}"'

        elif block_type == "repeat":
            repeat_count = "?"
            repeat_text = "?"

            if len(connections) > 1 and connections[1] in block_map:
                count_block = block_map[connections[1]]
                if isinstance(count_block[1], list) and count_block[1][0] == "divide":
                    count_connections = count_block[-1] if isinstance(count_block[-1], list) else []
                    num = get_numeric_value(count_connections[1] if len(count_connections) > 1 else None, block_map)
                    den = get_numeric_value(count_connections[2] if len(count_connections) > 2 else None, block_map)
                    if num is not None and den is not None and den != 0:
                        repeat_count = (num / den)
                        repeat_text = f"{num}/{den} = {repeat_count:.2f}"
                else:
                    repeat_count = get_numeric_value(connections[1], block_map)
                    repeat_text = str(repeat_count) if repeat_count is not None else "?"
            return f"Repeat ({repeat_text}) Times"

        elif block_type == "forever":
            return "Forever Loop (Repeats Indefinitely)"

        elif block_type == "penup":
            return "Pen Up (Lifts Pen from Canvas)"

        elif block_type == "pendown":
            return "Pen Down"

        elif block_type == "forward":
            forward_dist = get_numeric_value(connections[1] if len(connections) > 1 else None, block_map)
            return f"Move Forward → {forward_dist or '?'} Steps"

        elif block_type == "back":
            back_dist = get_numeric_value(connections[1] if len(connections) > 1 else None, block_map)
            return f"Move Backward → {back_dist or '?'} Steps"

        elif block_type == "right":
            right_angle = get_numeric_value(connections[1] if len(connections) > 1 else None, block_map)
            return f"Rotate Right → {right_angle or '?'}°"

        elif block_type == "left":
            left_angle = get_numeric_value(connections[1] if len(connections) > 1 else None, block_map)
            return f"Rotate Left → {left_angle or '?'}°"

        elif block_type == "setheading":
            heading = get_numeric_value(connections[1] if len(connections) > 1 else None, block_map)
            return f"Set Heading → {heading or '0'}°"

        elif block_type == "show":
            show_value = get_numeric_value(connections[2] if len(connections) > 2 else None, block_map)
            return f"Show Number: {show_value or '?'}"

        elif block_type == "increment":
            inc_color = get_numeric_value(connections[1] if len(connections) > 1 else None, block_map)
            inc_amount = get_numeric_value(connections[2] if len(connections) > 2 else None, block_map)
            return f"Increment --> Color: {inc_color or '?'}, Amount: {inc_amount or '?'}"

        elif block_type == "incrementOne":
            inc_one_var = get_named_box_value(connections[1] if len(connections) > 1 else None, block_map)
            return f'Increment Variable: "{inc_one_var or "?"}"'

        elif block_type == "newnote":
            return "Note"

        elif block_type == "playdrum":
            drum_name = get_drum_name(connections[1] if len(connections) > 1 else None, block_map)
            return f"Play Drum → {drum_name or '?'}"

        elif block_type == "arc":
            angle = "?"
            if len(connections) > 3 and connections[3] in block_map:
                angle_block = block_map[connections[3]]
                if isinstance(angle_block[1], list) and angle_block[1][0] == "divide":
                    angle_connections = angle_block[-1] if isinstance(angle_block[-1], list) else []
                    num = get_numeric_value(angle_connections[1] if len(angle_connections) > 1 else None, block_map)
                    den = get_numeric_value(angle_connections[2] if len(angle_connections) > 2 else None, block_map)
                    if num is not None and den is not None and den != 0:
                        angle = f"{(num / den):.2f}"
                else:
                    angle_val = get_numeric_value(connections[3], block_map)
                    angle = str(angle_val) if angle_val is not None else "?"

            radius = get_numeric_value(connections[2] if len(connections) > 2 else None, block_map)
            return f"Draw Arc --> Angle: {angle}°, Radius: {radius or '?'}"

        elif block_type == "print":
            print_text = get_text_value(connections[2] if len(connections) > 2 else None, block_map)
            return f'Print: "{print_text or ""}"'

        elif block_type == "plus":
            add1 = get_numeric_value(connections[1] if len(connections) > 1 else None, block_map)
            add2 = get_numeric_value(connections[2] if len(connections) > 2 else None, block_map)
            result = "?"
            if add1 is not None and add2 is not None:
                result = f"{(add1 + add2):.2f}"
            return f"Add --> {add1 or '?'} + {add2 or '?'} = {result}"

        elif block_type == "text":
            return f'"{block_args.get("value", "")}"'

        elif block_type == "pitch":
            solfege = "?"
            octave = get_numeric_value(connections[2] if len(connections) > 2 else None, block_map)

            if len(connections) > 1 and connections[1] in block_map:
                solfege_block = block_map[connections[1]]
                solfege_block_type = solfege_block[1][0] if isinstance(solfege_block[1], list) else solfege_block[1]

                if solfege_block_type == "text" and isinstance(solfege_block[1], list):
                    solfege = solfege_block[1][1].get('value', '?')
                elif solfege_block_type == "solfege" and isinstance(solfege_block[1], list):
                    solfege = solfege_block[1][1].get('value', '?')

            return f"Pitch --> Solfege: {solfege}, Octave: {octave or '?'}"

        elif block_type == "solfege":
            return None

        elif block_type == "nameddo":
            action_called = block_args.get('value', 'unnamed')
            return f'Do action --> "{action_called}"'

        elif block_type == "settransposition":
            transposition_value = get_numeric_value(connections[1] if len(connections) > 1 else None, block_map)
            return f"Set Transposition --> {transposition_value or '?'}"

        else:
            if isinstance(block_args, dict) and 'value' in block_args:
                return f"{block_type}: {block_args['value']}"
            return block_type[0].upper() + block_type[1:] if block_type else ""

    except Exception as e:
        return f"Error processing {block_type}: {str(e)}"


def process_block(
        block: List,
        block_map: Dict,
        visited: Set[str],
        indent: int = 1,
        is_clamp: bool = False,
        parent_block_type: Optional[str] = None
) -> List[str]:
    """Process a single block and its connections."""
    output = []
    block_id = block[0]

    if block_id in visited:
        return output

    visited.add(block_id)

    block_type = block[1]
    block_args = None
    if isinstance(block_type, list):
        block_args = block_type[1]
        block_type = block_type[0]

        if isinstance(block_args, dict):
            for key in block_args:
                if isinstance(block_args[key], str) and is_base64_data(block_args[key]):
                    block_args[key] = 'data'

    if block_type in ["vspace", "hidden"]:
        connections = block[-1] if isinstance(block[-1], list) else []
        for child_id in connections:
            if child_id in block_map:
                output.extend(process_block(block_map[child_id], block_map, visited, indent, is_clamp, block_type))
        return output

    if block_type in ["number", "drumname", "solfege"]:
        return output

    block_representation = get_block_representation(block_type, block_args, block, block_map, indent, is_clamp,
                                                    parent_block_type)
    if not block_representation:
        return output

    prefix = "│   " * (indent - 1) + "├── "
    output.append(f"{prefix}{block_representation}")

    connections = block[-1] if isinstance(block[-1], list) else []

    for i in range(len(connections) - 1):
        child_id = connections[i]
        if child_id is not None and child_id in block_map:
            child_block = block_map[child_id]
            child_block_type = child_block[1][0] if isinstance(child_block[1], list) else child_block[1]

            if not (child_block_type == "divide" and
                    (parent_block_type in ["newnote", "setmasterbpm2", "arc"])):
                output.extend(process_block(block_map[child_id], block_map, visited, indent + 1, True, block_type))

    if len(connections) > 0 and connections[-1] is not None:
        child_id = connections[-1]
        if child_id in block_map:
            output.extend(process_block(block_map[child_id], block_map, visited, indent, False, block_type))

    if block_type in ["start", "action"]:
        output.append("│   " * (indent - 1) + "│")

    return output


def convert_music_blocks(data: Union[List, Dict]) -> List[str]:
    """Convert Music Blocks JSON to text representation."""
    if not isinstance(data, list):
        return ["Invalid JSON format: Expected a list at the root."]

    if len(data) == 0:
        return ["Warning: No blocks found in input!"]

    output_lines = ["Start of Project"]
    block_map = {block[0]: block for block in data}
    visited = set()

    root_block = next((block for block in data
                       if (block[1][0] if isinstance(block[1], list) else block[1]) == "start"), data[0])

    output_lines.extend(process_block(root_block, block_map, visited, 1))

    for block in data:
        block_id = block[0]
        if block_id not in visited:
            block_type = block[1][0] if isinstance(block[1], list) else block[1]
            if block_type not in ["hidden", "vspace"] and block_id != root_block[0]:
                output_lines.extend(process_block(block, block_map, visited, 1))

    return output_lines

def main():
    """Main Streamlit application."""
    st.set_page_config(page_title="JSON to Text Representation", layout="wide")

    st.markdown("""
    <style>
        .stTextArea textarea {
            background-color: #2d2d2d !important;
            color: #f0f0f0 !important;
            border: 1px solid #3a3a3a !important;
            min-height: 300px !important;
            height: 300px !important;
        }

        .st-emotion-cache-1v0mbdj {
            display: flex;
            flex-direction: column;
            height: 100%;
        }

        .custom-label {
            color: #7f5af0 !important;
            font-weight: bold;
            margin-bottom: 8px;
            font-size: 0.95rem;
        }

        .stButton button {
            background-color: #7f5af0 !important;
            color: white !important;
            border: none;
            padding: 12px 20px;
            border-radius: 6px;
            cursor: pointer;
            font-size: 16px;
            transition: all 0.3s;
            font-weight: 500;
            width: 100%;
            margin-top: 10px;
        }
        .stButton button:hover {
            background-color: #6c4bd2 !important;
            transform: translateY(-1px);
        }
        .stButton button:active {
            transform: translateY(0);
        }

        #output-container {
            background-color: #2d2d2d;
            color: #f0f0f0;
            border: 1px solid #3a3a3a;
            border-radius: 6px;
            padding: 15px;
            min-height: 300px;
            height: 300px;
            overflow-y: auto;
            white-space: pre-wrap;
            font-family: monospace;
            margin-bottom: 10px;
        }

        h1 {
            color: #7f5af0;
            text-align: center;
            margin-bottom: 30px;
        }

        footer {
            margin-top: 40px;
            text-align: center;
            padding: 20px 0;
            color: #888;
            font-size: 0.9rem;
            border-top: 1px solid #3a3a3a;
        }
        footer a {
            color: #7f5af0;
            text-decoration: none;
            transition: color 0.3s;
        }
        footer a:hover {
            color: #6c4bd2;
            text-decoration: underline;
        }

        .copy-success {
            color: #2cb67d;
            font-weight: bold;
            margin-top: 10px;
            text-align: center;
        }

        .st-emotion-cache-1cypcdb {
            padding: 0 15px;
        }

        .st-emotion-cache-keje6w {
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True)

    st.title("Convert JSON to Text Representation")

    if 'output_text' not in st.session_state:
        st.session_state.output_text = "The text representation will appear here..."
    if 'json_input' not in st.session_state:
        st.session_state.json_input = ""

    col1, col2 = st.columns([1, 1], gap="medium")

    with col1:
        st.markdown('<div class="custom-label">Paste your JSON code here:</div>', unsafe_allow_html=True)
        json_input = st.text_area(
            "json_input_area",
            value=st.session_state.json_input,
            placeholder='Paste your project JSON here...',
            height=300,
            label_visibility="collapsed"
        )

        button_col1, button_col2 = st.columns([1, 1], gap="small")
        with button_col1:
            convert_clicked = st.button(
                "Convert to Text Representation",
                key="convert_btn",
                help="Convert the JSON to text representation"
            )

        with button_col2:
            clear_clicked = st.button(
                "Clear Input",
                key="clear_btn",
                help="Clear the input field"
            )

        if clear_clicked:
            st.session_state.json_input = ""
            st.session_state.output_text = "The text representation will appear here..."
            st.rerun()

    with col2:
        st.markdown('<div class="custom-label">Output:</div>', unsafe_allow_html=True)
        st.markdown(
            f'<div id="output-container">{st.session_state.output_text}</div>',
            unsafe_allow_html=True
        )

        copy_clicked = st.button(
            "Copy Output",
            key="copy_btn",
            help="Copy the output to clipboard"
        )

        if copy_clicked:
            try:
                pyperclip.copy(st.session_state.output_text)
                st.markdown('<div class="copy-success">Output copied to clipboard!</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Failed to copy text: {e}")

    if convert_clicked and json_input.strip():
        try:
            data = json.loads(json_input)
            text_representation = convert_music_blocks(data)
            st.session_state.output_text = "\n".join(text_representation)
            st.session_state.json_input = json_input
            st.rerun()
        except json.JSONDecodeError as e:
            st.session_state.output_text = f"Error: {str(e)}"
        except Exception as e:
            st.session_state.output_text = f"Error: {str(e)}"

    st.markdown("""
    <footer>
        <p>Created by <a href="https://github.com/omsuneri">Om Santosh Suneri</a></p>
    </footer>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
