import random

number_to_be_guessed = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100"))

if guess == number_to_be_guessed:
    print("You got it right")

else:
    print("Try again later, e fit be you next time, number to be guessed is ", number_to_be_guessed)

number_to_be_guessed = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100"))
number_of_guesses = 0

while number_of_guesses < 3:

    if guess == number_to_be_guessed:
        print("You got it right")
        break

    else:
        guess = int(input("guess a number between 1 and 100: "))
    number_of_guesses += 1

if number_of_guesses == 3:

    print("Try again later, e fit be you next time, number to be guessed is ", number_to_be_guessed)