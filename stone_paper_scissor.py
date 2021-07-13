import random
l=["Stone","Paper","Scissor"]
while(True):
    choice=str(input("Do you want to continue?(Y/N) "))
    if(choice=="y" or choice=="Y"):
        l1=random.choice(l)
        i=str(input("Enter your choice: "))
        print("Computer chose: ",l1)
        if((l1=="Stone" and i=="Paper") or (l1=="Paper" and i=="Scissor") or (l1=="Scissor" and i=="Stone")):
            print("YOU WIN!!!!!!!!!!!!")
        elif(l1==i):
            print("IT'S A TIE!!")
        else:
            print("BETTER LUCK NEXT TIME!!!")
    else:
        break
    
