import random

human_input = input('Pick Rock, Paper, or Scissors: ')
print('Human picked: ', human_input)

objects = ['Rock', 'Paper', 'Scissors']

computer_input = objects[random.randint(0,2)]
print('Computer picked: ', computer_input)

# Now the human and computer both pick an object. Now we will play the game
# -------------------------------------------------------------------------

if human_input == computer_input:
    print("Well that's a tie!")
elif human_input == 'Rock' and computer_input == 'Paper':
    print('Computer wins! Paper beats rock!')
elif human_input == 'Rock' and computer_input == 'Scissors':
    print('Humans beat the machines!')
elif human_input == 'Paper' and computer_input == 'Rock':
    print('Humans beat the machines!')
elif human_input == 'Paper' and computer_input == 'Scissors':
    print('Computer wins! Scissors cuts Paper!')
elif human_input == 'Scissors' and computer_input == 'Paper':
    print('Humans beat the machines!')
elif human_input == 'Scissors' and computer_input == 'Rock':
    print('Computer wins! Rock crushes Scissors')