import random

objects = ['Rock', 'Paper', 'Scissors']

Win_Condition = {'Rock': 'Scissors',
                 'Paper': 'Rock',
                 'Scissors': 'Paper',
                 }
Play_Again = True
while Play_Again is True:
    human_input = input('Pick Rock, Paper, or Scissors: ')
    print('Human picked: ', human_input)
    computer_input = objects[random.randint(0,2)]
    print('Computer picked: ', computer_input)
    if human_input == computer_input:
        print('Tie')
        Play_Again = input('Would you like to Play Again? (True/False): ')
    elif Win_Condition[human_input] == computer_input:
        print('Humans beat the Machines.')
        Play_Again = input('Would you like to Play Again? (True/False): ')
    else:
        print('AI Takeover.')
        Play_Again = input('Would you like to Play Again? (True/False): ')