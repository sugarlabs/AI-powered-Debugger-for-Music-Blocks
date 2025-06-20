Project 13. Test Suites 
 
Simplified Text Representation :  
 
Start of Project 
├── Start Block --> {ID: 1614725801114, Position: (0.00, 0.00), Heading: 
0°, Color: -10, Shade: 50, Pen Size: 5, Grey: 100.00} 
│   ├── EmptyHeap 
│   ├── Meter 
│   │   ├── Divide Block --> 1/4 = 0.25 
│   ├── Store Variable "box1" → 1 
│   ├── Do action --> "Music Tests 1" 
│   ├── Do action --> "Music Tests 2" 
│   ├── Do action --> "Music Tests 3" 
│   ├── Do action --> "Music Tests 4" 
│   ├── Do action --> "Maths Tests" 
│   ├── Do action --> "Graphics Tests" 
│   ├── ShowHeap 
│   ├── SaveHeap 
│   │   ├── "test-results.json" 
│ 
├── Setxy 
│   ├── Note 
│   │   ├── Action: "Graphics Tests" 
│   │   │   ├── "Graphics Tests" 
│   │   │ 
│   │   ├── Duration --> 1/4 = 0.25 
│   │   ├── Pitch --> Solfege: sol, Octave: 4 
│   │   ├── Print: "" 
│   │   │   ├── "Graphics Tests" 
├── Set Heading → 0° 
├── DoArg 
│   ├── "test xyh" 
├── Move Forward → 100 Steps 
├── Draw Arc --> Angle: ?°, Radius: 100 
├── DoArg 
│   ├── "test xyh" 
├── Setpensize 
├── Setcolor 
├── Move Forward → 100 Steps 
├── Move Backward → 50 Steps 
├── DoArg 
│   ├── "compare test" 
│   ├── getred: 100 
├── Setxy 
├── Set Heading → 0° 
├── x: 100 
├── equal: true 
│   ├── and: true 
│   │   ├── and: true 
│   │   │   ├── Ifthenelse 
│   │   │   │   ├── Action: "test xyh" 
│   │   │   │   │   ├── "test xyh" 
│   │   │   │   │ 
│   │   │   │   ├── Do action --> "passed" 
│   │   │   │   ├── Do action --> "failed" 
│   │   ├── equal: true 
│   │   │   ├── Arg 
│   │   ├── heading: 90 
│   ├── equal: true 
│   │   ├── Arg 
│   ├── y: 200 
│   ├── Arg 
├── Print: "" 
│   ├── Play Drum → clap 
│   │   ├── Note 
│   │   │   ├── Action: "passed" 
│   │   │   │   ├── "passed" 
│   │   │   │ 
│   │   │   ├── Duration --> 1/4 = 0.25 
│   │   ├── Push 
│   │   │   ├── Add --> ? + ? = ? 
│   │   │   │   ├── "Test " 
│   │   │   ├── Add --> ? + ? = ? 
│   │   │   │   ├── Variable: "box1" 
│   │   │   ├── " passed" 
│   │   ├── Increment Variable: "box1" 
│   │   │   ├── Variable: "box1" 
│   ├── Add --> ? + ? = ? 
│   │   ├── "Passed Test " 
│   ├── Variable: "box1" 
├── Print: "" 
│   ├── Play Drum → gong 
│   │   ├── Note 
│   │   │   ├── Action: "failed" 
│   │   │   │   ├── "failed" 
│   │   │   │ 
│   │   │   ├── Duration --> 1/1 = 1.00 
│   │   ├── Push 
│   │   │   ├── Add --> ? + ? = ? 
│   │   │   │   ├── "Test " 
│   │   │   ├── Add --> ? + ? = ? 
│   │   │   │   ├── Variable: "box1" 
│   │   │   ├── " failed" 
│   │   ├── Increment Variable: "box1" 
│   │   │   ├── Variable: "box1" 
│   ├── Add --> ? + ? = ? 
│   │   ├── "Failed Test " 
│   ├── Variable: "box1" 
├── Action: "compare test" 
│   ├── "compare test" 
│   ├── Ifthenelse 
│   │   ├── equal: true 
│   │   │   ├── Arg 
│   │   ├── Arg 
│   │   ├── Do action --> "passed" 
│   │   ├── Do action --> "failed" 
│ 
├── Action: "Maths Tests" 
│   ├── "Maths Tests" 
│   ├── Note 
│   │   ├── Duration --> 1/4 = 0.25 
│   │   ├── Pitch --> Solfege: sol, Octave: 4 
│   │   ├── Print: "" 
│   │   │   ├── "Maths Tests" 
│   ├── Setxy 
│   ├── DoArg 
│   │   ├── "compare test" 
│   │   ├── Distance 
│   │   │   ├── x: 100 
│   │   ├── y: 0 
│   ├── DoArg 
│   │   ├── "compare test" 
│   │   ├── Abs 
│   ├── DoArg 
│   │   ├── "compare test" 
│   │   ├── Sqrt 
│   ├── DoArg 
│   │   ├── "compare test" 
│   │   ├── Power 
│   ├── DoArg 
│   │   ├── "compare test" 
│   │   ├── Mod 
│   ├── DoArg 
│   │   ├── "compare test" 
│   │   ├── Int 
│   ├── DoArg 
│   │   ├── "compare test" 
│   │   ├── Int 
│   │   ├── "4" 
│ 
├── Note 
│   ├── Action: "Music Tests 1" 
│   │   ├── "Music Tests 1" 
│   │ 
│   ├── Duration --> 1/4 = 0.25 
│   ├── Pitch --> Solfege: sol, Octave: 4 
│   ├── Print: "" 
│   │   ├── "Music Tests 1" 
├── DoArg 
│   ├── "compare test" 
│   ├── mypitch: 7 
├── Note 
│   ├── Duration --> 1/4 = 0.25 
│   ├── Pitch --> Solfege: sol, Octave: 4 
├── DoArg 
│   ├── "compare test" 
│   ├── mynotevalue: 0.25 
│   ├── Divide Block --> 1/4 = 0.25 
├── Note 
│   ├── Duration --> 1/4 = 0.25 
│   ├── Pitch --> Solfege: ?, Octave: 4 
│   │   ├── notename: G 
├── Note 
│   ├── Duration --> 1/4 = 0.25 
│   ├── Steppitch 
├── DoArg 
│   ├── "compare test" 
│   ├── mypitch: 9 
├── Note 
│   ├── Duration --> 1/4 = 0.25 
│   ├── Pitchnumber 
├── DoArg 
│   ├── "compare test" 
│   ├── mypitch: 7 
├── Note 
│   ├── Duration --> 1/4 = 0.25 
│   ├── Nthmodalpitch 
├── DoArg 
│   ├── "compare test" 
│   ├── mypitch: 9 
├── Note 
│   ├── Duration --> 1/4 = 0.25 
│   ├── Pitch --> Solfege: la, Octave: 4 
├── Note 
│   ├── Duration --> 1/4 = 0.25 
│   ├── Pitch --> Solfege: sol, Octave: 4 
├── DoArg 
│   ├── "compare test" 
│   ├── deltapitch2: -1 
├── Note 
│   ├── Duration --> 1/4 = 0.25 
│   ├── Hertz 
├── DoArg 
│   ├── "compare test" 
│   ├── mypitch: 7 
├── Note 
│   ├── Duration --> 1/4 = 0.25 
│   ├── Hertz 
├── DoArg 
│   ├── "compare test" 
│   ├── Int 
│   ├── Add --> ? + 0.5 = ? 
│   │   ├── outputtools: pitch in hertz 
│   │   ├── currentpitch: G4 
├── Setpitchnumberoffset 
│   ├── notename: C 
├── DoArg 
│   ├── "compare test" 
│   ├── Number2pitch 
│   ├── notename: G 
├── Rhythmicdot2 
│   ├── Note 
│   │   ├── Duration --> 1/4 = 0.25 
│   │   ├── Pitch --> Solfege: sol, Octave: 4 
├── DoArg 
│   ├── "compare test" 
│   ├── mynotevalue: 0.375 
├── Multiplybeatfactor 
│   ├── Divide Block --> 1/2 = 0.50 
│   ├── Note 
│   │   ├── Duration --> 1/4 = 0.25 
│   │   ├── Pitch --> Solfege: sol, Octave: 4 
├── DoArg 
│   ├── "compare test" 
│   ├── mynotevalue: 0.125 
├── Setbpm3 
│   ├── Divide Block --> 1/4 = 0.25 
├── Osctime 
│   ├── Divide Block --> 1000/? = ? 
│   ├── Divide Block --> 3/2 = 1.50 
│   ├── Hertz 
├── DoArg 
│   ├── "compare test" 
│   ├── mynotevalue: 0.25 
├── Action: "Music Tests 2" 
│   ├── "Music Tests 2" 
│   ├── Note 
│   │   ├── Duration --> 1/4 = 0.25 
│   │   ├── Pitch --> Solfege: sol, Octave: 4 
│   │   ├── Print: "" 
│   │   │   ├── "Music Tests 2" 
│   ├── Store Variable "box" → ? 
│   │   ├── Elapsednotes2 
│   │   ├── Divide Block --> 1/4 = 0.25 
│   ├── Repeat (4) Times 
│   │   ├── Note 
│   │   │   ├── Duration --> 1/4 = 0.25 
│   │   │   ├── Pitch --> Solfege: sol, Octave: 4 
│   ├── DoArg 
│   │   ├── "compare test" 
│   │   ├── Minus 
│   │   │   ├── Elapsednotes2 
│   │   │   ├── Divide Block --> 1/4 = 0.25 
│   │   ├── Variable: "box" 
│   ├── Store Variable "box2" → ? 
│   │   ├── Int 
│   │   ├── beatvalue: 2.0060000000000002 
│   ├── Repeat (4) Times 
│   │   ├── Note 
│   │   │   ├── Duration --> 1/4 = 0.25 
│   │   │   ├── Play Drum → kick drum 
│   │   │   ├── Print: "" 
│   │   │   │   ├── Add --> ? + ? = ? 
│   │   │   │   │   ├── Variable: "box2" 
│   │   │   │   ├── Add --> ? + ? = ? 
│   │   │   │   │   ├── " " 
│   │   │   │   ├── Int 
│   │   │   │   ├── beatvalue: 2.0060000000000002 
│   │   ├── Increment Variable: "box2" 
│   │   │   ├── Variable: "box2" 
│   ├── DoArg 
│   │   ├── "compare test" 
│   │   ├── Int 
│   │   ├── beatvalue: 2.0060000000000002 
│   │   ├── Int 
│   │   ├── Mod 
│   │   │   ├── Variable: "box2" 
│   ├── DoArg 
│   │   ├── "compare test" 
│   │   ├── Hspace 
│   │   ├── Notecounter 
│   │   ├── Do action --> "whole note" 
│ 
├── Note 
│   ├── Action: "whole note" 
│   │   ├── "whole note" 
│   │ 
│   ├── Duration --> 1/1 = 1.00 
│   ├── Rest2 
├── Action: "Music Tests 3" 
│   ├── "Music Tests 3" 
│   ├── Setscalartransposition 
│   │   ├── Add --> 1 + ? = ? 
│   │   ├── Multiply 
│   │   │   ├── modelength: 7 
│   │   ├── Note 
│   │   │   ├── Duration --> 1/4 = 0.25 
│   │   │   ├── Pitch --> Solfege: sol, Octave: 4 
│   │   │   ├── Print: "" 
│   │   │   │   ├── "Music Tests 3" 
│   ├── Store Variable "box" → ? 
│   │   ├── outputtools: pitch class 
│   │   ├── currentpitch: A4 
│   ├── DoArg 
│   │   ├── "compare test" 
│   │   ├── Variable: "box" 
│ 
├── Neighbor2 
│   ├── Newstaccato 
│   │   ├── Newslur 
│   │   │   ├── Chorus 
│   │   │   │   ├── Vibrato 
│   │   │   │   │   ├── Tremolo 
│   │   │   │   │   │   ├── Phaser 
│   │   │   │   │   │   │   ├── Harmonic2 
│   │   │   │   │   │   │   │   ├── Dis 
│   │   │   │   │   │   │   │   │   ├── Print: "" 
│   │   │   │   │   │   │   │   │   │   ├── Action: "Music Tests 4" 
│   │   │   │   │   │   │   │   │   │   │   ├── "Music Tests 4" 
│   │   │   │   │   │   │   │   │   │   │ 
│   │   │   │   │   │   │   │   │   │   ├── "Tone and Ornament Tests" 
│   │   │   │   │   │   │   │   │   ├── Note 
│   │   │   │   │   │   │   │   │   │   ├── Duration --> 1/4 = 0.25 
│   │   │   │   │   │   │   │   │   │   ├── Note 
│   │   │   │   │   │   │   │   │   │   │   ├── Duration --> 1/4 = 0.25 
│   │   │   │   │   │   │   │   │   │   │   ├── Pitch --> Solfege: sol, 
Octave: 4 
│   │   │   │   │   │   │   │   │   │   ├── Pitch --> Solfege: sol, Octave: 
4 
│   │   │   │   │   │   │   │   ├── Note 
│   │   │   │   │   │   │   │   │   ├── Duration --> 1/4 = 0.25 
│   │   │   │   │   │   │   │   │   ├── Pitch --> Solfege: sol, Octave: 4 
│   │   │   │   │   │   │   ├── Note 
│   │   │   │   │   │   │   │   ├── Duration --> 1/4 = 0.25 
│   │   │   │   │   │   │   │   ├── Pitch --> Solfege: sol, Octave: 4 
│   │   │   │   │   │   ├── Note 
│   │   │   │   │   │   │   ├── Duration --> 1/4 = 0.25 
│   │   │   │   │   │   │   ├── Pitch --> Solfege: sol, Octave: 4 
│   │   │   │   │   ├── Divide Block --> 1/16 = 0.06 
│   │   │   │   │   ├── Note 
│   │   │   │   │   │   ├── Duration --> 1/4 = 0.25 
│   │   │   │   │   │   ├── Pitch --> Solfege: sol, Octave: 4 
│   │   │   │   ├── Note 
│   │   │   │   │   ├── Duration --> 1/4 = 0.25 
│   │   │   │   │   ├── Pitch --> Solfege: sol, Octave: 4 
│   │   │   ├── Divide Block --> 1/16 = 0.06 
│   │   │   ├── Note 
│   │   │   │   ├── Duration --> 1/4 = 0.25 
│   │   │   │   ├── Pitch --> Solfege: sol, Octave: 4 
│   │   │   ├── Note 
│   │   │   │   ├── Duration --> 1/4 = 0.25 
│   │   │   │   ├── Pitch --> Solfege: sol, Octave: 4 
│   │   ├── Divide Block --> 1/32 = 0.03 
│   │   ├── Note 
│   │   │   ├── Duration --> 1/4 = 0.25 
│   │   │   ├── Pitch --> Solfege: sol, Octave: 4 
│   ├── Divide Block --> 1/16 = 0.06 
│   ├── Note 
│   │   ├── Duration --> 1/4 = 0.25 
│   │   ├── Pitch --> Solfege: sol, Octave: 4 
├── Neighbor 
│   ├── Divide Block --> 1/16 = 0.06 
│   ├── Note 
│   │   ├── Duration --> 1/4 = 0.25 
│   │   ├── Pitch --> Solfege: sol, Octave: 4 
├── nameddoArg: compare test 
 
 
 
