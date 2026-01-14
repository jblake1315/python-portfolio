import random

# Game setup
print('===== Number Guessing Game =====')
print('I am thinking of a number between 1 and 100')
print()

# Generate random number
secret_number = random.randint(1, 100)
attempts = 0

# Game loop
while True:
    guess = int(input('Enter your guess: '))
    attempts = attempts + 1
    
    if guess < secret_number:
        print('Too low! Try again.')
    elif guess > secret_number:
        print('Too high! Try again.')
    else:
        print('Congratulations! You guessed it!')
        print('It took you', attempts, 'attempts.')
        break  # Exit the loop