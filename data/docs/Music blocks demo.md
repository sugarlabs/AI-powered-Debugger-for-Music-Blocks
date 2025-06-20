Project 11. Music blocks demo 
 
Simplified Text Representation :  
 
Start of Project 
├── Start Block --> {ID: 1623637935045, Position: (0.00, 0.00), Heading: 
0°, Color: 10, Shade: 60, Pen Size: 5, Grey: 185.71} 
│   ├── Switch 
│   │   ├── y: 100 
│   │   ├── Case 
│   │   │   ├── Do action --> "action" 
│   │   ├── Case 
│   │   │   ├── Do action --> "action1" 
│   │   ├── Defaultcase 
│   │   │   ├── Do action --> "action2" 
│ 
├── Action: "action" 
│   ├── "action" 
│   ├── Openpalette 
│   │   ├── "rhythm" 
│   ├── Pen Up (Lifts Pen from Canvas) 
│   ├── Setxy 
│   ├── Print: "" 
│   │   ├── "Welcome to Music Blocks" 
│   ├── Wait 
│   ├── Storein 
│   │   ├── "box" 
│   │   ├── Makeblock 
│   │   │   ├── "note" 
│   ├── Setxyturtle 
│   │   ├── "Mr. Mouse" 
│   ├── Runblock 
│   │   ├── Variable: "box" 
│   ├── Print: "" 
│   │   ├── "The Note Value block is at the heart of Music Blocks" 
│   ├── Wait 
│   ├── Print: "" 
│   │   ├── "If you change the note value to 8, you get an 1/8 note." 
│   ├── Deleteblock 
│   │   ├── Variable: "box" 
│   ├── Storein 
│   │   ├── "box" 
│   │   ├── Makeblock 
│   │   │   ├── "note" 
│   ├── Runblock 
│   │   ├── Variable: "box" 
│   ├── Wait 
│   ├── Print: "" 
│   │   ├── "If you change it to 2, you get a 1/2 note." 
│   ├── Deleteblock 
│   │   ├── Variable: "box" 
│   ├── Storein 
│   │   ├── "box" 
│   │   ├── Makeblock 
│   │   │   ├── "note" 
│   ├── Runblock 
│   │   ├── Variable: "box" 
│   ├── Wait 
│   ├── Print: "" 
│   │   ├── "You can also change the pitch inside a note." 
│   ├── Deleteblock 
│   │   ├── Variable: "box" 
│   ├── Storein 
│   │   ├── "box" 
│   │   ├── Makeblock 
│   │   │   ├── "note" 
│   ├── Setxyturtle 
│   │   ├── "Mr. Mouse" 
│   ├── Runblock 
│   │   ├── Variable: "box" 
│   ├── Wait 
│   ├── Print: "" 
│   │   ├── "Hit the Play Button to continue." 
│ 
├── Action: "action1" 
│   ├── "action1" 
│   ├── Deleteblock 
│   │   ├── Variable: "box" 
│   ├── Print: "" 
│   │   ├── "You can stack multiple notes together." 
│   ├── Storein 
│   │   ├── "box2" 
│   │   ├── Makeblock 
│   │   │   ├── "note" 
│   ├── Wait 
│   ├── Storein 
│   │   ├── "box3" 
│   │   ├── Makeblock 
│   │   │   ├── "note" 
│   ├── Dockblock 
│   │   ├── Variable: "box2" 
│   │   ├── Variable: "box3" 
│   ├── Wait 
│   ├── Storein 
│   │   ├── "box4" 
│   │   ├── Makeblock 
│   │   │   ├── "note" 
│   ├── Dockblock 
│   │   ├── Variable: "box3" 
│   │   ├── Variable: "box4" 
│   ├── Print: "" 
│   │   ├── "Listen to the stack of notes play from top to bottom." 
│   ├── Runblock 
│   │   ├── Variable: "box2" 
│   ├── Wait 
│   ├── Setxy 
│   ├── Wait 
│   ├── Print: "" 
│   │   ├── "Try adding more notes to the stack." 
│   ├── Wait 
│   ├── Print: "" 
│   │   ├── "Hit the Play Button to continue." 
│ 
├── Action: "action2" 
│   ├── "action2" 
│   ├── Print: "" 
│   │   ├── "Enjoy Music Blocks" 
│   ├── Setxy 
│   ├── Deleteblock 
│   │   ├── Variable: "box2" 
│   ├── Wait 
│   ├── Print: "" 
│   │   ├── "Click on the Play Button to replay this demo." 
│ 
├── Pen Up (Lifts Pen from Canvas) 
│   ├── Turtleshell 
│   │   ├── Setturtlename2 
│   │   │   ├── Start Block --> {ID: 1623637935081, Position: (-1000.00, 
-1000.00), Heading: 0°, Color: 20, Shade: 80, Pen Size: 5, Grey: 157.14} 
│   │   │   │ 
│   │   │   ├── "Mr. Mouse" 
│   │   ├── media: data 
├── Setxy 
 
 
