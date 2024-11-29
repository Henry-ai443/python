print("Select operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter your choice(1/2/3/4): ")

num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))

if choice == "1":
    print(f"{num_1} + {num_2} = {num_1 + num_2}")
elif choice == "2":
    print(f"{num_1} - {num_2} = {num_1 - num_2}")
elif choice == "3":
    print(f"{num_1} * {num_2} = {num_1 * num_2}")
elif choice == "4":
    if num_2 != 0:
        print(f"{num_1} / {num_2} = {num_1 / num_2}")
    else:
        print("Error!Division by zero.")
else:
    print("Invalid input!")