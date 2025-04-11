import random

emojis = {
    'rock': '🤘',
    'paper': '📃',
    'scissor': '✂',
    'r': '🤘',
    'p': '📃',
    's': '✂'
}

choices = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissor',
    'rock': 'rock',
    'paper': 'paper',
    'scissor': 'scissor'
}

options = ['rock', 'paper', 'scissor']

while True:
    user_input = input("Rock, Paper, or Scissor? (r/p/s): ").lower()

    if user_input not in choices:
        print("Invalid choice. Try again.")
        continue

    user = choices[user_input]
    computer = random.choice(options)

    print(f'You chose {user.capitalize()} {emojis[user_input]}')
    print(f'Computer chose {computer.capitalize()} {emojis[computer]}')

    if user == computer:
        print("It's a tie!\n")
    elif (user == 'rock' and computer == 'scissor') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissor' and computer == 'paper'):
        print("You win!\n")
    else:
        print("You lose!\n")

    should_continue = input('Continue(y/n: )').lower()
    if should_continue == 'n':
        break
