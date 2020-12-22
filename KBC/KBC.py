from playsound import playsound
import time
print("\t\t:::::::::::::::::::* * * WELCOME TO KBC...!!! * * * :::::::::::::::::::::::::")
playsound('Kbc main theme.mp3')
print("\n\n\t............   Kon Bane ga Caror      ............")
print("*.*.*."*20)
name=input("ENTER YOUR NAME =")
points=0
questions={
    1:["When was Python released ?","1990","1800","1991","1875"],  
    2:["Who developed Python ?","Guido Van Rossum","Ross","Luis Bruno","Chadvic"], 
    3:["Python got its name from which show ?","Food Fly","I-Tech.","Snakes","Monty Python's Flying Circus"],
    4:["In how many ways, can you work in Python ?","Interactive mode","Script Mode","Both A) and B)","None Of These."], 
    5:["Which of the following are not valid strings in Python ?","''Hello''","'Hello'","'Hello''","'''Hello'''"], 
    6:["What is use to create empty list -","list()","()","Both A) and B)","None Of These."], 
    7:["What is use to create empty tuple -","tuple()","()","Both A) and B)","None Of These."], 
    8:["Out-put of the code -\n\ta=(1,2,3,4,5,6,7,8,9,10)\n\tprint(len())","8","9","10","ERROR"], 
    9:["Out put of the code -\n\ta=(1,2,3,4,5,6,7,8,9,10)\n\tprint(a[::-1])","(10, 9, 8, 7, 6, 5, 4, 3, 2, 1)","(1,2,3,4,5,6,7,8,9,10)","((10, 9, 8, 7, 6, 5, 4, 3, 2, 1))","ERROR"], 
    10:["According to computer Python is an -","Interpretator","compiler","High level languare (as compare to C++, C+, etc.)","Snake"]
     }
answers={1:"C",2:"A",3:"D",4:"C",5:"C", 6:"A",7:"C",8:"C",9:"A",10:"A"}
for i in range(1,11) :
    print("......"*20)
    print("Q)",i," ",questions[i][0])
    playsound('KBC question.mp3')
    print("\n\tA)  ",questions[i][1])
    print("\tB)  ",questions[i][2])
    print("\tC)  ",questions[i][3])
    print("\tD)  ",questions[i][4])
    start_1=time.process_time()
    answer=input("Enter Your Option :-")
    if answer.upper()==answers[i] :
        print("****"*20)
        print("\nCORRECT ANSWER....!!!\n+2 POINTS !!")
        playsound('right answer.mp3')
        points=points+2
        print("\nTOTAL POINTS =",points)
        print("TOTAL TIME TAKEN(till now) =",time.process_time(),)
        print("****"*20)
    else :
        print("****"*20)
        print("\nWRONG ANSWER.....!!!\n-1 POINTS !!")
        playsound('wrong answer.mp3')
        points=points-1
        print("\nTOTAL POINTS =",points)
        print("TOTAL TIME TAKEN(till now) =",time.process_time(),)
        print("****"*20)
print("\n\n\n\n===="*20)
print("\t\t::::::::::::    GAME OVER...!!    :::::::::::::")
print("\n\t",name.upper(),"YOUR TOTAL SCORE IS =",points)
print("\tTOTAL TIME TAKEN(till now) =",time.process_time())
playsound('game over.wav')
