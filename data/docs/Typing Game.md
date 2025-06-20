Project 14. Typing Game 
 
Simplified Text Representation :  
 
Start of Project 
├── Start Block --> {ID: 1711709201283, Position: (0.00, 0.00), Heading: 
0°, Color: 70, Shade: 60, Pen Size: 5, Grey: 71.43} 
│   ├── Setturtlename2 
│   │   ├── "mainmouse" 
│   ├── Drift 
│   │   ├── Pen Up (Lifts Pen from Canvas) 
│   │   ├── Setturtlename2 
│   │   │   ├── "mainmouse" 
│   │   ├── Setxy 
│   │   ├── Turtleshell 
│   │   │   ├── media: data 
│   │   ├── Listen 
│   │   │   ├── myclick: null 
│   │   │   ├── "start" 
│ 
├── Random 
│   ├── Storein 
│   │   ├── Storein 
│   │   │   ├── Pen Up (Lifts Pen from Canvas) 
│   │   │   │   ├── Wait 
│   │   │   │   │   ├── Print: "" 
│   │   │   │   │   │   ├── Action: "start" 
│   │   │   │   │   │   │   ├── "start" 
│   │   │   │   │   │   │ 
│   │   │   │   │   │   ├── "Make sure caps lock is on before you begin; 
type letter and press return." 
│   │   │   ├── "result" 
│   │   ├── "random" 
│   ├── Storein 
│   │   ├── "letter" 
│   │   ├── Toascii 
│   │   ├── Variable: "random" 
│   ├── Dispatch 
│   │   ├── "input" 
│   ├── Dispatch 
│   │   ├── "fall" 
├── Wait 
│   ├── Store Variable "fall" → ? 
│   │   ├── Move Backward → 5 Steps 
│   │   │   ├── Show Number: ? 
│   │   │   │   ├── Setcolor 
│   │   │   │   │   ├── Turtleshell 
│   │   │   │   │   │   ├── While 
│   │   │   │   │   │   │   ├── Setxy 
│   │   │   │   │   │   │   │   ├── Storein 
│   │   │   │   │   │   │   │   │   ├── Pen Up (Lifts Pen from Canvas) 
│   │   │   │   │   │   │   │   │   │   ├── Drift 
│   │   │   │   │   │   │   │   │   │   │   ├── Turtleshell 
│   │   │   │   │   │   │   │   │   │   │   │   ├── Pen Up (Lifts Pen from 
Canvas) 
│   │   │   │   │   │   │   │   │   │   │   │   │   ├── Action: 
"fallalphabet" 
│   │   │   │   │   │   │   │   │   │   │   │   │   │   ├── "fallalphabet" 
│   │   │   │   │   │   │   │   │   │   │   │   │   │ 
│   │   │   │   │   │   │   │   │   │   │   │   ├── media: data 
│   │   │   │   │   │   │   │   │   ├── "fall" 
│   │   │   │   │   │   │   │   ├── Variable: "fall" 
│   │   │   │   │   │   │   ├── and: null 
│   │   │   │   │   │   │   │   ├── not_equal_to: null 
│   │   │   │   │   │   │   │   │   ├── Variable: "result" 
│   │   │   │   │   │   │   ├── greater_than_or_equal_to: null 
│   │   │   │   │   │   │   │   ├── Variable: "fall" 
│   │   │   │   │   │   ├── media: data 
│   │   │   │   ├── Variable: "letter" 
│   │   ├── Minus 
│   │   │   ├── Variable: "fall" 
├── Erasemedia 
├── If 
│   ├── less_than_or_equal_to: null 
│   │   ├── Variable: "fall" 
│   ├── Clear 
│   ├── Print: "" 
│   │   ├── "Game Over" 
│   ├── Wait 
├── Setxy 
│   ├── Action: "takeinput" 
│   │   ├── "takeinput" 
│   │ 
├── Pen Up (Lifts Pen from Canvas) 
├── Drift 
│   ├── While 
│   │   ├── not_equal_to: null 
│   │   │   ├── Variable: "result" 
│   │   ├── Input 
│   │   │   ├── "Letter ?" 
│   │   ├── Ifthenelse 
│   │   │   ├── equal: null 
│   │   │   │   ├── inputvalue: null 
│   │   │   ├── Variable: "letter" 
│   │   │   ├── Do action --> "correct" 
│   │   │   ├── Do 
│   │   │   │   ├── "start" 
│   │   │   ├── Do action --> "incorrect" 
├── Note 
│   ├── Settimbre 
│   │   ├── Action: "correct" 
│   │   │   ├── "correct" 
│   │   │ 
│   │   ├── voicename: electronic synth 
│   ├── Duration --> 2/4 = 0.50 
│   ├── Print: "" 
│   │   ├── Add --> ? + ? = ? 
│   │   │   ├── "The keyboard number for that letter "" 
│   │   ├── Add --> ? + ? = ? 
│   │   │   ├── Variable: "letter" 
│   │   ├── Add --> ? + ? = ? 
│   │   │   ├── "" is : " 
│   │   ├── Variable: "random" 
│   ├── Pitchnumber 
│   │   ├── Mod 
│   │   │   ├── Variable: "random" 
├── Store Variable "result" → 1 
├── Pen Up (Lifts Pen from Canvas) 
├── Erasemedia 
├── Wait 
├── Play Drum → hi hat 
│   ├── Play Drum → crash 
│   │   ├── Note 
│   │   │   ├── Action: "incorrect" 
│   │   │   │   ├── "incorrect" 
│   │   │   │ 
│   │   │   ├── Duration --> 2/4 = 0.50 
├── Play Drum → gong 
├── Listen 
│   ├── Setxy 
│   │   ├── Turtleshell 
│   │   │   ├── Pen Up (Lifts Pen from Canvas) 
│   │   │   │   ├── Drift 
│   │   │   │   │   ├── Setturtlename2 
│   │   │   │   │   │   ├── Start Block --> {ID: 1711733470987, Position: 
(0.00, 0.00), Heading: 0°, Color: -10, Shade: 60, Pen Size: 5, Grey: 
100.00} 
│   │   │   │   │   │   │ 
│   │   │   │   │   │   ├── "inputmouse" 
│   │   │   ├── media: data 
│   ├── "input" 
│   ├── "takeinput" 
├── Listen 
│   ├── Setxy 
│   │   ├── Turtleshell 
│   │   │   ├── Pen Up (Lifts Pen from Canvas) 
│   │   │   │   ├── Drift 
│   │   │   │   │   ├── Setturtlename2 
│   │   │   │   │   │   ├── Start Block --> {ID: 1711734642444, Position: 
(0.00, 0.00), Heading: 0°, Color: 70, Shade: 60, Pen Size: 5, Grey: 71.43} 
│   │   │   │   │   │   │ 
│   │   │   │   │   │   ├── "fallmouse" 
│   │   │   ├── media: data 
│   ├── "fall" 
│   ├── "fallalphabet" 
