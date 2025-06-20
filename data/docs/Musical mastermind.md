Project 8. Musical mastermind 
 
Simplified Text Representation :  
 
Start of Project 
├── Start Block --> {ID: 1642954990391, Position: (300.00, -400.00), 
Heading: 0°, Color: 40, Shade: 0, Pen Size: 1, Grey: 50.00} 
│   ├── Setturtlename2 
│   │   ├── "test" 
│   ├── Clear 
│   ├── Pen Up (Lifts Pen from Canvas) 
│   ├── Setxy 
│   ├── Show Number: ? 
│   │   ├── height: 1292 
│   │   ├── media: data 
│   ├── Setxy 
│   ├── Show Number: ? 
│   │   ├── media: data 
│   ├── Setxy 
│   ├── Setpensize 
│   ├── Turtleshell 
│   │   ├── media: data 
│   ├── Storein 
│   │   ├── "active mouse" 
│   │   ├── "" 
│   ├── EmptyHeap 
│   ├── Do action --> "push a note" 
│   ├── Do action --> "push a note" 
│   ├── Do action --> "push a note" 
│   ├── Do action --> "push a note" 
│   ├── Listen 
│   │   ├── myclick: click1642954990391 
│   │   ├── "test action" 
│   ├── Print: "" 
│   │   ├── "Select a mouse, then click on a note." 
│ 
├── Note 
│   ├── Dispatch 
│   │   ├── Action: "broadcast event" 
│   │   │   ├── "broadcast event" 
│   │   │ 
│   │   ├── turtlename: ti 
│   ├── Duration --> 1/4 = 0.25 
│   ├── Ifthenelse 
│   │   ├── equal: false 
│   │   │   ├── turtlename: ti 
│   │   ├── "drum" 
│   │   ├── Play Drum → hi hat 
│   │   ├── Pitch --> Solfege: ?, Octave: 4 
│   │   │   ├── turtlename: ti 
├── Store Variable "active mouse" → ? 
│   ├── If 
│   │   ├── Action: "make active" 
│   │   │   ├── "make active" 
│   │   │ 
│   │   ├── greater: true 
│   │   │   ├── height: 1292 
│   │   ├── Print: "" 
│   │   │   ├── "Select a note" 
│   ├── turtlename: two 
├── Storein 
│   ├── turtlename: two 
├── Start Block --> {ID: 1642955104985, Position: (-150.00, -400.00), 
Heading: 0°, Color: -10, Shade: 50, Pen Size: 5, Grey: 100.00} 
│   ├── Setturtlename2 
│   │   ├── "one" 
│   ├── Pen Up (Lifts Pen from Canvas) 
│   ├── Setxy 
│   ├── Do action --> "common events" 
│ 
├── Start Block --> {ID: 1642955106668, Position: (-300.00, 170.00), 
Heading: 0°, Color: -10, Shade: 0, Pen Size: 5, Grey: 100.00} 
│   ├── Setturtlename2 
│   │   ├── "do" 
│   ├── Pen Up (Lifts Pen from Canvas) 
│   ├── Setxy 
│   ├── Listen 
│   │   ├── myclick: click1642955106668 
│   │   ├── "broadcast event" 
│   ├── Do action --> "setup" 
│ 
├── "make active" 
├── Listen 
│   ├── Turtleshell 
│   │   ├── Action: "common events" 
│   │   │   ├── "common events" 
│   │   │ 
│   │   ├── media: data 
│   ├── mycursorover: CursorOver1642957037345 
├── Listen 
│   ├── "do" 
│   ├── "do action" 
├── Listen 
│   ├── "re" 
│   ├── "re action" 
├── Listen 
│   ├── "mi" 
│   ├── "mi action" 
├── Listen 
│   ├── "fa" 
│   ├── "fa action" 
├── Listen 
│   ├── "sol" 
│   ├── "sol action" 
├── Listen 
│   ├── "la" 
│   ├── "la action" 
├── Listen 
│   ├── "ti" 
│   ├── "ti action" 
├── Listen 
│   ├── "drum" 
│   ├── "drum action" 
├── Listen 
│   ├── "test" 
│   ├── "backup" 
├── Start Block --> {ID: 1642955193067, Position: (-50.00, -400.00), 
Heading: 0°, Color: -10, Shade: 50, Pen Size: 5, Grey: 100.00} 
│   ├── Setturtlename2 
│   │   ├── "two" 
│   ├── Pen Up (Lifts Pen from Canvas) 
│   ├── Setxy 
│   ├── Do action --> "common events" 
│ 
├── If 
│   ├── Action: "do action" 
│   │   ├── "do action" 
│   │ 
│   ├── equal: false 
│   │   ├── Variable: "active mouse" 
│   ├── turtlename: four 
│   ├── Storein 
│   │   ├── turtlename: one 
│   │   ├── "do" 
├── Start Block --> {ID: 1642955681394, Position: (-200.00, 178.00), 
Heading: 0°, Color: -10, Shade: 0, Pen Size: 5, Grey: 100.00} 
│   ├── Setturtlename2 
│   │   ├── "re" 
│   ├── Pen Up (Lifts Pen from Canvas) 
│   ├── Setxy 
│   ├── Listen 
│   │   ├── myclick: click1642955681394 
│   │   ├── "broadcast event" 
│   ├── Do action --> "setup" 
│ 
├── Start Block --> {ID: 1642955682647, Position: (-100.00, 185.00), 
Heading: 0°, Color: -10, Shade: 0, Pen Size: 5, Grey: 100.00} 
│   ├── Setturtlename2 
│   │   ├── "mi" 
│   ├── Pen Up (Lifts Pen from Canvas) 
│   ├── Setxy 
│   ├── Listen 
│   │   ├── myclick: click1642955682647 
│   │   ├── "broadcast event" 
│   ├── Do action --> "setup" 
│ 
├── Start Block --> {ID: 1642955683564, Position: (-1.00, 194.00), Heading: 
0°, Color: -10, Shade: 0, Pen Size: 5, Grey: 100.00} 
│   ├── Setturtlename2 
│   │   ├── "fa" 
│   ├── Pen Up (Lifts Pen from Canvas) 
│   ├── Setxy 
│   ├── Listen 
│   │   ├── myclick: click1642955683564 
│   │   ├── "broadcast event" 
│   ├── Do action --> "setup" 
│ 
├── Start Block --> {ID: 1642955684337, Position: (100.00, 202.00), 
Heading: 0°, Color: -10, Shade: 0, Pen Size: 5, Grey: 100.00} 
│   ├── Setturtlename2 
│   │   ├── "sol" 
│   ├── Pen Up (Lifts Pen from Canvas) 
│   ├── Setxy 
│   ├── Listen 
│   │   ├── myclick: click1642955684337 
│   │   ├── "broadcast event" 
│   ├── Do action --> "setup" 
│ 
├── Start Block --> {ID: 1642955685803, Position: (200.00, 210.00), 
Heading: 0°, Color: -10, Shade: 0, Pen Size: 5, Grey: 100.00} 
│   ├── Setturtlename2 
│   │   ├── "la" 
│   ├── Pen Up (Lifts Pen from Canvas) 
│   ├── Setxy 
│   ├── Listen 
│   │   ├── myclick: click1642955685803 
│   │   ├── "broadcast event" 
│   ├── Do action --> "setup" 
│ 
├── Start Block --> {ID: 1642955687994, Position: (300.00, 220.00), 
Heading: 0°, Color: -10, Shade: 0, Pen Size: 5, Grey: 100.00} 
│   ├── Setturtlename2 
│   │   ├── "ti" 
│   ├── Pen Up (Lifts Pen from Canvas) 
│   ├── Setxy 
│   ├── Listen 
│   │   ├── myclick: click1642955687994 
│   │   ├── "broadcast event" 
│   ├── Do action --> "setup" 
│ 
├── x: 360 
├── Increment --> Color: ?, Amount: 15 
│   ├── Show Number: ? 
│   │   ├── Setxy 
│   │   │   ├── Storein 
│   │   │   │   ├── Increment --> Color: ?, Amount: -15 
│   │   │   │   │   ├── Setshade 
│   │   │   │   │   │   ├── Ifthenelse 
│   │   │   │   │   │   │   ├── Action: "setup" 
│   │   │   │   │   │   │   │   ├── "setup" 
│   │   │   │   │   │   │   │ 
│   │   │   │   │   │   │   ├── equal: true 
│   │   │   │   │   │   │   │   ├── turtlename: drum 
│   │   │   │   │   │   │   ├── "drum" 
│   │   │   │   │   │   │   ├── Turtleshell 
│   │   │   │   │   │   │   │   ├── media: data 
│   │   │   │   │   │   │   ├── Turtleshell 
│   │   │   │   │   │   │   │   ├── media: data 
│   │   │   │   │   ├── x: 375 
│   │   │   │   ├── turtlename: drum 
│   │   │   │   ├── y: 194 
│   │   │   ├── x: 360 
│   │   ├── turtlename: drum 
├── Setxy 
│   ├── x: 375 
│   ├── Box 
│   ├── turtlename: drum 
├── Action: "ti action" 
│   ├── "ti action" 
│   ├── If 
│   │   ├── equal: false 
│   │   │   ├── Variable: "active mouse" 
│   │   ├── turtlename: four 
│   │   ├── Storein 
│   │   │   ├── turtlename: two 
│   │   │   ├── "ti" 
│ 
├── Action: "la action" 
│   ├── "la action" 
│   ├── If 
│   │   ├── equal: false 
│   │   │   ├── Variable: "active mouse" 
│   │   ├── turtlename: four 
│   │   ├── Storein 
│   │   │   ├── turtlename: three 
│   │   │   ├── "la" 
│ 
├── Action: "sol action" 
│   ├── "sol action" 
│   ├── If 
│   │   ├── equal: false 
│   │   │   ├── Variable: "active mouse" 
│   │   ├── turtlename: four 
│   │   ├── Storein 
│   │   │   ├── turtlename: two 
│   │   │   ├── "sol" 
│ 
├── Action: "fa action" 
│   ├── "fa action" 
│   ├── If 
│   │   ├── equal: false 
│   │   │   ├── Variable: "active mouse" 
│   │   ├── turtlename: four 
│   │   ├── Storein 
│   │   │   ├── turtlename: three 
│   │   │   ├── "fa" 
│ 
├── Action: "mi action" 
│   ├── "mi action" 
│   ├── If 
│   │   ├── equal: false 
│   │   │   ├── Variable: "active mouse" 
│   │   ├── turtlename: four 
│   │   ├── Storein 
│   │   │   ├── turtlename: one 
│   │   │   ├── "mi" 
│ 
├── Action: "re action" 
│   ├── "re action" 
│   ├── If 
│   │   ├── equal: false 
│   │   │   ├── Variable: "active mouse" 
│   │   ├── turtlename: four 
│   │   ├── Storein 
│   │   │   ├── turtlename: one 
│   │   │   ├── "re" 
│ 
├── Action: "test action" 
│   ├── "test action" 
│   ├── Dispatch 
│   │   ├── "test" 
│   ├── Storein 
│   │   ├── "win" 
│   ├── Pen Up (Lifts Pen from Canvas) 
│   ├── Setxy 
│   │   ├── y: -300 
│   ├── Pen Down 
│   ├── Store Variable "box1" → 1 
│   ├── Store Variable "box2" → ? 
│   │   ├── Box 
│   │   ├── "one" 
│   ├── Do action --> "test box" 
│   ├── Store Variable "box1" → 2 
│   ├── Store Variable "box2" → ? 
│   │   ├── Box 
│   │   ├── "two" 
│   ├── Do action --> "test box" 
│   ├── Store Variable "box1" → 3 
│   ├── Store Variable "box2" → ? 
│   │   ├── Box 
│   │   ├── "three" 
│   ├── Do action --> "test box" 
│   ├── Store Variable "box1" → 4 
│   ├── Store Variable "box2" → ? 
│   │   ├── Box 
│   │   ├── "four" 
│   ├── Do action --> "test box" 
│   ├── Pen Up (Lifts Pen from Canvas) 
│   ├── Setxy 
│   │   ├── y: -300 
│   ├── Move Backward → 100 Steps 
│   ├── If 
│   │   ├── equal: true 
│   │   │   ├── Variable: "win" 
│   │   ├── Drift 
│   │   │   ├── Do action --> "dance" 
│ 
├── Start Block --> {ID: 1642957036597, Position: (50.00, -400.00), 
Heading: 0°, Color: -10, Shade: 50, Pen Size: 5, Grey: 100.00} 
│   ├── Setturtlename2 
│   │   ├── "three" 
│   ├── Pen Up (Lifts Pen from Canvas) 
│   ├── Setxy 
│   ├── Do action --> "common events" 
│ 
├── Start Block --> {ID: 1642957037345, Position: (150.00, -400.00), 
Heading: 0°, Color: -10, Shade: 50, Pen Size: 5, Grey: 100.00} 
│   ├── Setturtlename2 
│   │   ├── "four" 
│   ├── Pen Up (Lifts Pen from Canvas) 
│   ├── Setxy 
│   ├── Do action --> "common events" 
│ 
├── Move Forward → 80 Steps 
│   ├── Repeat (4) Times 
│   │   ├── Fill 
│   │   │   ├── Setgrey 
│   │   │   │   ├── Setcolor 
│   │   │   │   │   ├── Action: "green" 
│   │   │   │   │   │   ├── "green" 
│   │   │   │   │   │ 
├── Rotate Right → 90° 
├── Setcolor 
│   ├── Action: "yellow" 
│   │   ├── "yellow" 
│   │ 
├── Setgrey 
├── Fill 
│   ├── Repeat (4) Times 
│   │   ├── Move Forward → 80 Steps 
│   │   ├── Rotate Right → 90° 
├── Setcolor 
│   ├── Action: "gray" 
│   │   ├── "gray" 
│   │ 
├── Setgrey 
├── Fill 
│   ├── Repeat (4) Times 
│   │   ├── Move Forward → 80 Steps 
│   │   ├── Rotate Right → 90° 
├── Push 
│   ├── Ifthenelse 
│   │   ├── Action: "push a note" 
│   │   │   ├── "push a note" 
│   │   │ 
│   │   ├── equal: true 
│   │   ├── Random 
│   │   ├── Push 
│   │   │   ├── "drum" 
│   ├── Random 
├── Action: "test box" 
│   ├── "test box" 
│   ├── Note 
│   │   ├── Duration --> 1/4 = 0.25 
│   │   ├── Ifthenelse 
│   │   │   ├── equal: true 
│   │   │   │   ├── Variable: "box2" 
│   │   │   ├── "drum" 
│   │   │   ├── Play Drum → hi hat 
│   │   │   ├── Pitch --> Solfege: ?, Octave: 4 
│   │   │   │   ├── Variable: "box2" 
│   ├── Ifthenelse 
│   │   ├── equal: true 
│   │   │   ├── Variable: "box2" 
│   │   ├── IndexHeap 
│   │   ├── Variable: "box1" 
│   │   ├── Do action --> "green" 
│   │   ├── Store Variable "win" → 0 
│   │   ├── Store Variable "box" → 0 
│   │   ├── If 
│   │   │   ├── equal: false 
│   │   │   │   ├── Variable: "box2" 
│   │   │   ├── IndexHeap 
│   │   │   ├── Store Variable "box" → 1 
│   │   ├── If 
│   │   │   ├── equal: false 
│   │   │   │   ├── Variable: "box2" 
│   │   │   ├── IndexHeap 
│   │   │   ├── Store Variable "box" → 1 
│   │   ├── If 
│   │   │   ├── equal: false 
│   │   │   │   ├── Variable: "box2" 
│   │   │   ├── IndexHeap 
│   │   │   ├── Store Variable "box" → 1 
│   │   ├── If 
│   │   │   ├── equal: false 
│   │   │   │   ├── Variable: "box2" 
│   │   │   ├── IndexHeap 
│   │   │   ├── Store Variable "box" → 1 
│   │   ├── Ifthenelse 
│   │   │   ├── equal: false 
│   │   │   ├── Variable: "box" 
│   │   │   ├── Do action --> "yellow" 
│   │   │   ├── Do action --> "gray" 
│   ├── Setshade 
│   ├── Pen Up (Lifts Pen from Canvas) 
│   ├── Increment --> Color: ?, Amount: 5 
│   │   ├── x: 110 
│   ├── Increment --> Color: ?, Amount: 12 
│   │   ├── y: -300 
│   ├── Show Number: ? 
│   │   ├── Variable: "box2" 
│   ├── Increment --> Color: ?, Amount: -5 
│   │   ├── x: 115 
│   ├── Increment --> Color: ?, Amount: -12 
│   │   ├── y: -288 
│   ├── Increment --> Color: ?, Amount: 100 
│   │   ├── x: 110 
│   ├── Pen Down 
│ 
├── Action: "backup" 
│   ├── "backup" 
│   ├── Move Backward → 100 Steps 
│ 
├── Action: "dance" 
│   ├── "dance" 
│   ├── Repeat (4) Times 
│   │   ├── Set Transposition --> ? 
│   │   │   ├── Multiply 
│   │   │   │   ├── Random 
│   │   │   ├── Note 
│   │   │   │   ├── Duration --> 1/4 = 0.25 
│   │   │   │   ├── Ifthenelse 
│   │   │   │   │   ├── equal: false 
│   │   │   │   │   │   ├── Box 
│   │   │   │   │   │   ├── "one" 
│   │   │   │   │   ├── "drum" 
│   │   │   │   │   ├── Play Drum → hi hat 
│   │   │   │   │   ├── Pitch --> Solfege: ?, Octave: 4 
│   │   │   │   │   │   ├── Box 
│   │   │   │   │   │   ├── "one" 
│   │   │   ├── Note 
│   │   │   │   ├── Duration --> 1/4 = 0.25 
│   │   │   │   ├── Ifthenelse 
│   │   │   │   │   ├── equal: false 
│   │   │   │   │   │   ├── Box 
│   │   │   │   │   │   ├── "two" 
│   │   │   │   │   ├── "drum" 
│   │   │   │   │   ├── Play Drum → hi hat 
│   │   │   │   │   ├── Pitch --> Solfege: ?, Octave: 4 
│   │   │   │   │   │   ├── Box 
│   │   │   │   │   │   ├── "two" 
│   │   │   ├── Note 
│   │   │   │   ├── Duration --> 1/4 = 0.25 
│   │   │   │   ├── Ifthenelse 
│   │   │   │   │   ├── equal: false 
│   │   │   │   │   │   ├── Box 
│   │   │   │   │   │   ├── "three" 
│   │   │   │   │   ├── "drum" 
│   │   │   │   │   ├── Play Drum → hi hat 
│   │   │   │   │   ├── Pitch --> Solfege: ?, Octave: 4 
│   │   │   │   │   │   ├── Box 
│   │   │   │   │   │   ├── "three" 
│   │   │   ├── Note 
│   │   │   │   ├── Duration --> 1/4 = 0.25 
│   │   │   │   ├── Ifthenelse 
│   │   │   │   │   ├── equal: true 
│   │   │   │   │   │   ├── Box 
│   │   │   │   │   │   ├── "four" 
│   │   │   │   │   ├── "drum" 
│   │   │   │   │   ├── Play Drum → hi hat 
│   │   │   │   │   ├── Pitch --> Solfege: ?, Octave: 4 
│   │   │   │   │   │   ├── Box 
│   │   │   │   │   │   ├── "four" 
│ 
├── Start Block --> {ID: 1644022037786, Position: (375.00, 195.00), 
Heading: 0°, Color: -10, Shade: 0, Pen Size: 5, Grey: 100.00} 
│   ├── Setturtlename2 
│   │   ├── "drum" 
│   ├── Pen Up (Lifts Pen from Canvas) 
│   ├── Setxy 
│   ├── Listen 
│   │   ├── myclick: click1644022037786 
│   │   ├── "broadcast event" 
│   ├── Do action --> "setup" 
│ 
├── Action: "drum action" 
│   ├── "drum action" 
│   ├── If 
│   │   ├── equal: true 
│   │   │   ├── Variable: "active mouse" 
│   │   ├── turtlename: four 
│   │   ├── Storein 
│   │   │   ├── turtlename: four 
│   │   │   ├── "drum" 
│ 
 
