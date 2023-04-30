import random
print("WELCOME TO THE GAME GUESS THE NUMBER")
att = 3
#m = int(input("Enter the range from 1 to :"))
n = random.randint(1,15)
while att:
    u_guess = int(input("Enter your number"))
    if u_guess < n-5:
        print("Too small")
    elif u_guess < n-3:
        print("Reaching")
    elif u_guess > n+3:
        print("Gone")
    elif u_guess > n+5:
        print("Too far")
    elif u_guess == n:
        print("Reached, Well done")
        
    att-=1
if att==11:
    print("Oops ! Sorry You Have Lost...")
