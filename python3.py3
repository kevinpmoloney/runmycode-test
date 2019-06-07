import sys
import random

print('Hello World from Python 3!')    
    
# get a random number 1-100, then
# build a prompt to ask for the users nth guess.
# respond appropriately
rn=random.randint(1,100)
NumberOfGuesses=0
GuessedIt=False

# where to loop??????????

rn=randint(1,100)
While GuessedIt<>True:
    NumberOfGuesses += 1
    if(NumberOfGuesses=1):
        GuessNo="1st"
    elif(NumberOfGuesses=2):
        GuessNo="2nd":
    elif(NumberOfGuesses=3):
        GuessNo="3rd"
    else:
        GuessNo=str(NumberOfGuesses) + "th"
    print("Enter your " + GuessNo + " guess: ")
    
    # get users guess and act accordingly
    resp=input()
    if (int(resp)=rn):
        GuessedIt=True
        Print("You are correct, sir!")
    elif (int(resp)>rn:
        Print("Higher...")
    else:
        Print("Lower...")
    while strcont<>"print("Do you wanr to play again? \(Y\/N\): ")
          
    

