import random

def guess_the_number():
    print("Welcome to the number guessing game!")
    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Enter any number between 1 and 100: ")
        attempts += 1
        if number == " ":
            print("This field is mandatory for you to continue!!")
        elif guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")

        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts")
            break
guess_the_number()