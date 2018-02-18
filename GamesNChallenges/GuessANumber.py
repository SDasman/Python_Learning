#Guess a Number
import random
number = random.randint(0,20)
guess_number = 0 # number of guesses taken by user.
user = int(input('Guess a random number between 0 and 20: '))
Win = False  # boolean is set to false. User hasn't won the game yet.
while Win is False:
    guess_number += 1
    if user == number:
        Win = True
        print('Wow congrats! You got it after ' + str(guess_number) + ' guesses.')
    elif user > number:
        print('Keep trying. Go Lower.')
        user = int(input('Guess a random number between 0 and 20: '))
    elif user < number:
        print('Keep trying. Go Higher.')
        user = int(input('Guess a random number between 0 and 20: '))