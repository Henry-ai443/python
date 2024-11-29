# program to check if a number is even or odd
while True:
    num = int(input("Enter a number and I'll tell you if its EVEN or ODD: "))
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")