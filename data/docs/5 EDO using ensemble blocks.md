Project 10. 5 EDO using ensemble blocks 
 
Simplified Text Representation :  
 
Start of Project 
├── Start Block --> {ID: 1713408573598, Position: (-600.00, 0.00), Heading: 
0°, Color: -10, Shade: 60, Pen Size: 5, Grey: 100.00} 
│   ├── Store Variable "box1" → 1 
│   ├── Pen Up (Lifts Pen from Canvas) 
│   ├── Setxy 
│   ├── Do action --> "prompt" 
│   ├── Repeat (?) Times 
│   │   ├── Variable: "box2" 
│   │   ├── Do action --> "set" 
│   │   ├── Do action --> "preview" 
│   │   ├── Do action --> "next" 
│   ├── Setxy 
│   ├── Turtleshell 
│   │   ├── media: data 
│   ├── Listen 
│   │   ├── myclick: click1713408573598 
│   │   ├── "play all" 
│ 
├── Newturtle 
│   ├── Action: "set" 
│   │   ├── "set" 
│   │ 
│   ├── Variable: "box1" 
├── Wait 
├── Setturtle 
│   ├── Int 
│   ├── Variable: "box1" 
│   ├── Pen Up (Lifts Pen from Canvas) 
│   ├── Listen 
│   │   ├── myclick: click1713414139382 
│   │   ├── "play" 
├── Setxyturtle 
│   ├── Int 
│   ├── Variable: "box1" 
│   ├── x: -123.60679774997914 
│   ├── y: -380.42260651806146 
├── Draw Arc --> Angle: ?°, Radius: 400 
│   ├── Action: "next" 
│   │   ├── "next" 
│   │ 
│   ├── Divide Block --> 360/? = ? 
│   ├── Variable: "box2" 
├── Increment Variable: "box1" 
│   ├── Variable: "box1" 
├── Note 
│   ├── Settimbre 
│   │   ├── Drift 
│   │   │   ├── Action: "play" 
│   │   │   │   ├── "play" 
│   │   │   │ 
│   │   ├── voicename: piano 
│   ├── Duration --> 1/4 = 0.25 
│   ├── Hertz 
│   │   ├── Multiply 
│   │   │   ├── outputtools: pitch in hertz 
│   │   ├── Power 
│   │   ├── Divide Block --> ?/? = ? 
│   │   │   ├── Int 
│   │   │   ├── turtlename: 5 
│   │   ├── Variable: "box2" 
├── Print: "" 
│   ├── Add --> ? + ? = ? 
│   │   ├── "Pitch in hertz: " 
│   ├── Add --> ? + ? = ? 
│   │   ├── Int 
│   │   ├── outputtools: pitch in hertz 
│   │   ├── currentpitch: C6 
│   ├── Add --> ? + ? = ? 
│   │   ├── " and its nearest pitch is " 
│   ├── outputtools: alphabet 
│   ├── currentpitch: C6 
├── " equal divisions of the octave." 
├── Add --> ? + ? = ? 
│   ├── Add --> ? + ? = ? 
│   │   ├── Print: "" 
│   │   │   ├── Wait 
│   │   │   │   ├── Store Variable "box2" → ? 
│   │   │   │   │   ├── Input 
│   │   │   │   │   │   ├── Print: "" 
│   │   │   │   │   │   │   ├── Action: "prompt" 
│   │   │   │   │   │   │   │   ├── "prompt" 
│   │   │   │   │   │   │   │ 
│   │   │   │   │   │   │   ├── "Choose how many equal divisions of the 
octave you would like." 
│   │   │   │   │   │   ├── "Input a value" 
│   │   │   │   │   ├── inputvalue: 5 
│   │   ├── "You are in a temperament system of " 
│   ├── Variable: "box2" 
├── Action: "preview" 
│   ├── "preview" 
│   ├── Settimbre 
│   │   ├── voicename: piano 
│   │   ├── Note 
│   │   │   ├── Duration --> 1/4 = 0.25 
│   │   │   ├── Pitch --> Solfege: do, Octave: 2 
│   │   │   ├── Hertz 
│   │   │   │   ├── Multiply 
│   │   │   │   │   ├── outputtools: pitch in hertz 
│   │   │   │   ├── Power 
│   │   │   │   ├── Divide Block --> ?/? = ? 
│   │   │   │   │   ├── Variable: "box1" 
│   │   │   │   ├── Variable: "box2" 
│ 
├── Action: "play all" 
│   ├── "play all" 
│   ├── Store Variable "box1" → 1 
│   ├── Repeat (?) Times 
│   │   ├── Variable: "box2" 
│   │   ├── Do action --> "preview" 
│   │   ├── Increment Variable: "box1" 
│   │   │   ├── Variable: "box1" 
│ 
├── Start Block --> {ID: 1713414131106, Position: (-400.00, 0.00), Heading: 
0°, Color: -10, Shade: 60, Pen Size: 5, Grey: 100.00} 
│   ├── Setturtlename2 
│   │   ├── "1" 
│ 
├── Start Block --> {ID: 1713414133449, Position: (-123.61, 380.42), 
Heading: 0°, Color: -10, Shade: 60, Pen Size: 5, Grey: 100.00} 
│   ├── Setturtlename2 
│   │   ├── "2" 
│ 
├── Start Block --> {ID: 1713414135421, Position: (323.61, 235.11), 
Heading: 0°, Color: -10, Shade: 60, Pen Size: 5, Grey: 100.00} 
│   ├── Setturtlename2 
│   │   ├── "3" 
│ 
├── Start Block --> {ID: 1713414137420, Position: (323.61, -235.11), 
Heading: 0°, Color: -10, Shade: 60, Pen Size: 5, Grey: 100.00} 
│   ├── Setturtlename2 
│   │   ├── "4" 
│ 
├── Start Block --> {ID: 1713414139382, Position: (-123.61, -380.42), 
Heading: 0°, Color: -10, Shade: 60, Pen Size: 5, Grey: 100.00} 
│   ├── Setturtlename2 
│   │   ├── "5" 
│ 
 
