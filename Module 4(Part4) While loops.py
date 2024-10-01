import random

random_number = random.randint(1, 10)

while True:
    try:

        guess = int(input("Guess the number between 1 and 10: "))
        if guess > random_number:
            print("Too high!")
        elif guess < random_number:
            print("Too low!")
        else:
            print("Correct! You guessed the right number!")
            break
    except ValueError:
        print("Please enter a valid integer!")
