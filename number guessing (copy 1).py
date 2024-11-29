import random
number = random.randint(1, 100)
guess = 0

while guess != number:
    guess = int(input("Enter any random number: "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("CORRECT!")
