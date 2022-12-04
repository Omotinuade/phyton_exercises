import random

count = 0
number_to_be_guessed = random.randint(1, 100)
user_input = input("Welcome, how about we play a guessing game? (yes/ no): ")
option_1 = "yes"
option_2 = "no"
while user_input != option_1 and user_input != option_2:
    print("Kindly try again with a Yes or No response!")
    user_input = input("Welcome, how about we play a guessing game? (yes/ no): ")

if user_input.lower() == option_1:
    while count < 3:
        guess = int(input("Guess a random number between 1 and 100: "))
        if guess == number_to_be_guessed:
            print("Congratulations, you got it right!")
            break
        else:
            if guess > number_to_be_guessed:
                print("Oops! You are wrong", "Your guess is too high", sep="\n")
            else:
                print("Oops! You are wrong", "Your guess is too low", sep="\n")

            count += 1
        if count == 3:
            print("Better luck next time!", "The number you could not guess right is", number_to_be_guessed, sep="\n")
elif user_input.lower() == option_2:
    print("You could have won #50,000, see you next time!")

