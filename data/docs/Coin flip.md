Project 7. Coin flip 
 
Simplified Text Representation :  
 
Start of Project 
├── Start Block --> {ID: 1659360734366, Position: (0.00, 0.00), Heading: 
0°, Color: -10, Shade: 60, Pen Size: 5, Grey: 100.00} 
│   ├── Settimbre 
│   │   ├── voicename: vibraphone 
│   │   ├── Print: "" 
│   │   │   ├── "Let's start!" 
│   │   ├── Note 
│   │   │   ├── Duration --> 1/1 = 1.00 
│   │   │   ├── Pitch --> Solfege: do, Octave: 3 
│   │   ├── Drift 
│   │   │   ├── Repeat (10) Times 
│   │   │   │   ├── Print: "" 
│   │   │   │   │   ├── "Let's flip a coin!" 
│   │   │   │   ├── Store Variable "box1" → ? 
│   │   │   │   │   ├── OneOf 
│   │   │   │   │   │   ├── "heads" 
│   │   │   │   │   ├── "tails" 
│   │   │   │   ├── Repeat (4) Times 
│   │   │   │   │   ├── Do action --> "spin" 
│   │   │   │   ├── Note 
│   │   │   │   │   ├── Duration --> 1/2 = 0.50 
│   │   │   │   │   ├── Do 
│   │   │   │   │   │   ├── Variable: "box1" 
│   │   │   │   ├── Note 
│   │   │   │   │   ├── Duration --> 1/2 = 0.50 
│   │   │   │   │   ├── Print: "" 
│   │   │   │   │   │   ├── Add --> ? + ? = ? 
│   │   │   │   │   │   │   ├── "The result of the coinflip was " 
│   │   │   │   │   │   ├── Variable: "box1" 
│   │   │   │   │   ├── Push 
│   │   │   │   │   │   ├── Variable: "box1" 
│   │   │   ├── ReverseHeap 
│   │   │   ├── Print: "" 
│   │   │   │   ├── Add --> ? + ? = ? 
│   │   │   │   │   ├── "The results are " 
│   │   │   │   ├── heap: null 
│ 
├── Action: "heads" 
│   ├── "heads" 
│   ├── Turtleshell 
│   │   ├── media: data 
│   ├── Pitch --> Solfege: do, Octave: 4 
│ 
├── Action: "tails" 
│   ├── "tails" 
│   ├── Turtleshell 
│   │   ├── media: data 
│   ├── Pitch --> Solfege: fa♯, Octave: 4 
│   ├── Pitch --> Solfege: sol, Octave: 4 
│ 
├── Turtleshell 
│   ├── Note 
│   │   ├── Action: "spin" 
│   │   │   ├── "spin" 
│   │   │ 
│   │   ├── Duration --> 1/20 = 0.05 
│   ├── Note 
│   │   ├── Duration --> 1/20 = 0.05 
│   │   ├── Turtleshell 
│   │   │   ├── media: data 
│   │   ├── Steppitch 
│   ├── Note 
│   │   ├── Duration --> 1/20 = 0.05 
│   │   ├── Turtleshell 
│   │   │   ├── media: data 
│   │   ├── Steppitch 
│   ├── Note 
│   │   ├── Duration --> 1/20 = 0.05 
│   │   ├── Turtleshell 
│   │   │   ├── media: data 
│   │   ├── Steppitch 
│   ├── Note 
│   │   ├── Duration --> 1/20 = 0.05 
│   │   ├── Turtleshell 
│   │   │   ├── media: data 
│   │   ├── Steppitch 
│   ├── media: data 
├── Steppitch 
 
 
