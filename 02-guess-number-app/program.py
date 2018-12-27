import random


def get_guess(question):
    try:
        return int(input(question))
    except ValueError:
        print('That does not appear to be an integer')
        get_guess(question)


number = random.randint(1, 100)
guess = get_guess(f'Guess a number between 1 and 100: ')

while guess != number:
    direction = 'higher' if guess < number else 'lower'
    guess = get_guess(f'Sorry {guess} need to be {direction}, guess again: ')

print(f'You got it! The number is {number}!')
