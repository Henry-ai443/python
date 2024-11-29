import random

def quizgame():
    print("Welcome to the computer quiz game: ")
    playing = input("Do you want to play? ")
    score = 0
    print()

    if playing != "yes":
        quit()
    else:
        print("Okay let us play")
        print()
    answer = input("What does RAM stand for: ")
    if answer == "random access memory":
        print("Correct")
        score += 1
    else:
        print("INCORRECT!!")
        print("The correct answer is: Random Access Memory")

    answer = input("What does ROM stand for: ")
    if answer == "read only memory":
        print("CORRECT")
        score += 1
    else:
        print("INCORRECT!!")
        print("Read Only Memory")

    answer = input("What does CPU stand for: ")
    if answer == "central processing unit":
        print("CORRECT")
        score += 1
    else:
        print("INCORRECT!!")
        print("The correct answer is: Central Processing Unit")

    answer = input("What does PSU stand for: ")
    if answer == "power supply unit":
        print("CORRECT")
        score += 1
    else:
        print("INCORRECT!!")
        print("The correct answer is Power Supply Unit ")
    
    answer = input("What does GPU stand for: ")
    if answer == "graphics processing unit":
        print("CORRECT")
        score += 1
    else:
        print("INCORRECT!!")

    print(f"You got {score} questions correct")
    print(f"Your percentage score is { score / 5 * 100}%")

def guess_the_number():
    print("Welcome to the number guessing game!")
    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Enter any number between 1 and 100: "))
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
        