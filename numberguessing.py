
import random
answer="y"
while answer=="y":
    secret_number=random.randint(1,100)
    attempts=0
    while True:
        try:
        
            guess=int(input("Enter your guess from 1 to 100!\n"))
            attempts+=1
            if guess == secret_number:
                print("You Guessed it Right !!")
                print(f"You took {attempts} attempts to complete the game")
                answer=input("Do you want to play again!if yes please press y or n for no!").lower()
                break
            elif guess < secret_number:
                print("Try Higher")
            elif guess > secret_number:
                print("Try Lesser")
        
        except:
            print("Invalid guess! Try Again")



