import random
number = random.randint(1,9);
chances = 0
print('Number guessing game');
print('Guess a number (between 1 and 9): ');
while chances<5:
    guess = input('Enter you guess: ');
    chances=chances+1
    if int(guess) < number:
        print('Your number is too low, try again')
    if int(guess) > number:
        print('Your number is too high, try again')
    if int(guess) == number:
        print('Congratulations! You Won!')
        break
if not chances<5:
    print("YOU LOSE! The number was " + str(number));