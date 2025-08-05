#!/usr/bin/env python3


"""Number Guessing Game | Step 1"""

import random 


# Generate a random number between 1 and 10
secret_number = random.randint(1,10)

#Ask for user input 
guess= int(input("Guess the number between 1 and 10: "))

#check if the guess is correct 
if guess < 1 or guess > 10:
    print("Dude you are tripping. Follow the rules")

elif guess == secret_number:
    print("Bit you guessed it! You was right!")

elif guess > secret_number:
    print("too much dip")

elif guess< secret_number:
    print("not enough chip")
    
