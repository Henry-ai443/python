grades = []

while True:
    grade = input("Enter a grade(type 'done' to finish): ")
    if grade.lower() == "done":
        break
    else:
        grades.append(float(grade))

average = (sum(grades)) / len(grades)
print (f"Your average grade is {average}")