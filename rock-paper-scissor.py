import random
print("WELCOME TO THE GAME - ROCK, PAPER, SCISSOR")
print("RULES : \n 1. Rock beats the Scissor \n 2. Paper beats the Rock \n 3. Scissor beats the Paper \n ")
n = input("Enter your choice (Rock , Paper, Scissor) : ")
actions = ["Rock, Paper, Scissor"]
c = random.choice(actions)
print()

if n==c:
    print("OH! Its a tie")
elif n == "Rock":
    if c=="Scissor":
        print("Rock beats the scissor,\n You win !")
    else :
        print("Paper covers the rock \n You lose !")
elif n=="Paper":
    if c == "Rock":
        print("paper covers the rock \n You win !")
        
    else :
        print("sciossor cuts the paper \n You lose !")
elif n == "Scissor":
    if c=="Paper":
        print("Scissor cuts the paper \n You win!")
    else:
        print("Rock beats the scissor \n You lose !")
    
    
