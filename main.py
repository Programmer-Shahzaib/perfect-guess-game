# --------------------------------Project 2----------------------------
# ------------------------------THE PERFECT GUESS----------------------
import random as r
name=input("Enter Your name: ",)
print(f"Welcome! {name} into our Game : THE PERFECT GUESS")
while(True):
    Exact_Number=r.randint(1,100)
    print(f"Lets Start the Game:")
    Guesses=0
    while(True):
        guess=int(input("Guess the number (between 1 and 100): ",))
        Guesses+=1
        if guess>Exact_Number:
            print ("Lower number please")
        elif guess<Exact_Number:
            print ("Higher number please")
        else:
            print(f"🎉 Correct! You guessed it right ")
            print(f"Exact Number= {Exact_Number}")
            print(f"User Guess= {guess}")
            print(f"User guess the number in {Guesses} attempts")
            break
    choice=input("Do you want to play again? (yes/no): ",).lower()
    if choice=="yes":
        continue
    else:
        break
print("Thanks for playing our Game!")
print("Game Over!")
