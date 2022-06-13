import random,time

userScore = 0
compScore = 0

choices = ['R', 'P', 'S']

rnd = 1

while True:
    print("Round: ", rnd)
    userChoice = input ("What do you wanna pick (R)ock, (P)aper, (S)cissor?")
    compChoice = random.choice(choices)
    print("Computer chose:", compChoice)

    if len(userChoice) == 0:
        print("Invalid answer, Try again")
        time.sleep(1)
        continue

    if userChoice.islower()==False:
        userChoice = userChoice.upper()
    else:
        print("User input should be in Capital Letter")
        continue

    if userChoice[0].upper() == compChoice:
        print("Draw!")
        time.sleep(1)
        continue
    
    elif userChoice[0].upper()=="R" and compChoice =="S":
        print("User Wins this round!")
        time.sleep(1)
        userScore = userScore + 1
    elif userChoice[0].upper()=="R" and compChoice =="P":
        print("Computer Wins this round!")
        time.sleep(1)
        compScore = compScore + 1
    elif userChoice[0].upper()=="S" and compChoice =="P":
        print("User Wins this round!")
        time.sleep(1)
        userScore = userScore + 1
    elif userChoice[0].upper()=="S" and compChoice =="R":
        print("Computer Wins this round!")
        time.sleep(1)
        compScore = compScore + 1
    elif userChoice[0].upper()=="P" and compChoice =="S":
        print("Computer Wins this round!")
        time.sleep(1)
        compScore = compScore + 1
    elif userChoice[0].upper()=="P" and compChoice =="R":
        print("User Wins this round!")
        time.sleep(1)
        userScore = userScore + 1
    else:
        print("Invalid answer, Try again!")
        continue

    rnd = rnd + 1
    if rnd == 6:
        break
    
print("User Wins: ", userScore)
print("Computer Wins: ", compScore)

if userScore > compScore:
    print("The User Wins the game!")
elif compScore > userScore:
    print("The Computer Wins the game!")
else:
    print("Draw!")
