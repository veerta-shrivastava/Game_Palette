import random
def Quiz():
    print("1.Science")
    print("2.General Knowledge")
    print("3.History")
        
        
    user=int(input("Enter subject(1-3):"))
    if user==1:
        point=0
        print("1.How many bones are present in human body?")
        a1=input("Answer:").lower()
        if a1=="206":
            point+=1
            print("Correct!")
        else:
            print("INCORRECT. The correct answer is 206")
        print("2.What is the hardest natural substance in Earth?")
        a2=input("Answer:").lower()
        if a2=="diamond":
            point+=1
            print("Correct!")
        else:
            print("INCORRECT. The correct answer is Diamond")
        print("3.Which element is the best conductor of electricity?")
        a3=input("Answer:").lower()
        if a3=="silver":
            point+=1
            print("Correct!")
        else:
            print("INCORRECT. The correct answer is Silver.")
        print("4.Which planet is closest to Sun?")
        a4=input("Answer:").lower()
        if a4=="mercury":
            point+=1
            print("Correct!")
        else:
            print("INCORRECT. The correct answer is Mercury.")
        print("5.What is the heaviest organ in human body?")
        a5=input("Answer:").lower()
        if a5=="liver":
            point+=1
            print("Correct!")
        else:
            print("INCORRECT. The correct answer is Liver.")
        print("points:",point)
    
    if user==2:
        point=0
        print("1.Who is the country's first citizen?")
        a1=input("Answer:").lower()
        if a1=="president":
            point+=1
            print("Correct!")
        else:
            print("INCORRECT. The correct answer is President")
        print("2.What is emergency number for fire?")
        a2=input("Answer:").lower()
        if a2=="101":
            point+=1
            print("Correct!")
        else:
            print("INCORRECT. The correct answer is 101")
        print("3.First female Prime Minister of India?")
        a3=input("Answer:").lower()
        if a3=="pratibha patil":
            point+=1
            print("Correct!")
        else:
            print("INCORRECT. The correct answer is Pratibha Patil")
        print("4.Which lines demarcates boundary between India and China?")
        a4=input("Answer:").lower()
        if a4=="mcmohan line":
            point+=1
            print("Correct!")
        else:
            print("INCORRECT. The correct answer is McMohan Line.")
        print("5.Which continent has the longest river in the world?")
        a5=input("Answer:").lower()
        if a5=="africa":
            point+=1
            print("Correct!")
        else:
            print("INCORRECT. The correct answer is Africa.")
        print("points:",point)

    elif user==3:
        point=0
        print("1.What is the modern name of Patliputra?")
        a1=input("Answer:").lower()
        if a1=="patna":
            point+=1
            print("Correct!")
        else:
            print("INCORRECT. The correct answer is Patna")
        print("2.Tipu Sultan was the ruler of?")
        a2=input("Answer:").lower()
        if a2=="mysore":
            point+=1
            print("Correct!")
        else:
            print("INCORRECT. The correct answer is Mysore.")
        print("3.When was the battle of Waterloo fought?")
        a3=input("Answer:").lower()
        if a3=="1815":
            point+=1
            print("Correct!")
        else:
            print("INCORRECT. The correct answer is 1815.")
        print("4.The Mughal Empire reached its peak under the rule of which emperor?")
        a4=input("Answer:").lower()
        if a4=="akbar":
            point+=1
            print("Correct!")
        else:
            print("INCORRECT. The correct answer is Akbar")
        print("5.When did the first world war end?")
        a5=input("Answer:").lower()
        if a5=="1918":
            point+=1
            print("Correct!")
        else:
            print("INCORRECT. The correct answer is 1918")
        print("points:",point)
def High_Low():
    number=random.randint(1,100)
        
    print("In this game user guesses a number from 1 to 100 and is told if its higher or lower until correct.")
    while True:
        guess=int(input("Your guess:"))
        if guess<1 or guess>100:
            print("Enter number between 1 to 100")
            continue
        if guess==number:
            print("YOU WON!")
            break
        elif guess<number:
            print("Higher")
        elif guess>number:
            print("Lower")
        else:
            print("Invalid input")
def Rock_Paper_Scissor():
    CompChoice=random.randint(1,3)
    d={1:"Rock",2:"Paper",3:"Scissor"}
        
    User=int(input("Choose(1:Rock,2:Paper,3:Scissor):"))
    print("Computer chose:", d[CompChoice])
    if CompChoice==User:
        print("Computer chose:",d[CompChoice])
        print("Its a tie.")
    elif (CompChoice == 1 and User == 2) or (CompChoice == 2 and User == 3) or (CompChoice == 3 and User == 1):
        print("You Won!")
    else:
        print("You Lost!")

def Hangman():
    print("Try to guess the word in less than 10 attempts")
    wordlist=["india","bollywood","rhythm","education"]
    word=random.choice(wordlist)
    turns=10
    guessmade=" "
    validentry=set("qwertyuioplkjhgfdsazxcvbnm")
    while turns>0:
        mainword=""
        missed=0
        for letter in word:
            if letter in guessmade:
                mainword+=letter
            else:
                mainword=mainword+" _ "
        if mainword==word:
            print(mainword)
            print("YOU WON")
            break
        print("Guess the word", mainword)
        guess=input("Enter:")
        if guess in validentry:
            guessmade=guessmade+guess
        else:
            guess=input("Enter valid character:")
        if guess not in word:
            turns-=1
            if turns==9:
                print("--------------")
                print("9 turns left")
            elif turns==8:
                print("8 turns left")
                print("--------------")
                print("       o      ")
            elif turns==7:
                print(r"7 turns left")
                print(r"---------------")
                print(r"       o       ")
                print(r"       |       ")
            elif turns==6:
                print("6 turns left")
                print(r"---------------")
                print(r"       o       ")
                print(r"       |       ")
                print(r"      /        ")
            elif turns==5:
                print(r"5 turns left")
                print(r"---------------")
                print(r"       o       ")
                print(r"       |       ")
                print(r"      / \      ")
            elif turns==4:
                print("4 turns left")
                print(r"---------------")
                print(r"      \o       ")
                print(r"       |       ")
                print(r"      / \      ")
            elif turns==3:
                print("3 turns left")
                print("---------------")
                print(r"      \o/      ")
                print(r"       |       ")
                print(r"      / \      ")
            elif turns==2:
                print("2 turns left")
                print("---------------")
                print(r"      \o/ |    ")
                print(r"       |       ")
                print(r"      / \      ")
            elif turns==1:
                print("only 1 turns left!! Hangman on its last breath.")
                print("---------------")
                print(r"      \o/_|    ")
                print(r"       |       ")
                print(r"      / \      ")
            elif turns==0:
                print("You loose")
                print("You let a good man die!!")
                
                
                
            

                







#Main
print("GAME PALETTE!!")
print("-"*100)
print("-"*100)
PlayGame=True
while PlayGame==True:
    print("1:HangMan")
    print("2:High and Low")
    print("3:Rock Paper Scissor")
    print("4:Quiz")
    
    GameChoice=int(input("Enter the game you want to play(1-4):"))
    print()
    print()
    if GameChoice==4:
        Quiz()
    elif GameChoice==2:
        High_Low()
    elif GameChoice==3:
        Rock_Paper_Scissor()
    elif GameChoice==1:
        Hangman()
    else:
        print("Invalid Input")
    print()
    print()
    ContinuePlaying=input("Do you want to Play again(yes/no):")
    if ContinuePlaying.lower()in ["yes","y"]:
        PlayGame=True 
    else:
        PlayGame=False
        print("-"*100)
        print("-"*100)
        print("Thank you for playing!")


