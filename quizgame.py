print("Welcome to my computer quiz game.")

score = 0 
playing=input("Do you want to play (q to quit)? ")
if playing.lower() == "yes":
    print("Okay let us play")
else:
    quit()

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT")

answer = input("What does ROM stand for? ")
if answer.lower() == "read only memory":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT")

answer = input("What does SSD stand for? ")
if answer.lower() == "solid state drive":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT")

answer = input("What does HDD stand for? ")
if answer.lower() == "hard disk drive":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT")

print(f"You got {score} questions correct")
print(f"Your score is {score / 5 * 100}%")
