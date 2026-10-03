# question-12: take three numbers as input. print the largest of the three without using any built-in function.
a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if a > b:
    if a > c:
        print(f"{a} is the greatest.")
    else:
        print(f"{c} is the greatest.")
else:
    if b > c:
        print(f"{b} is the greatest.")
    else:
        print(f"{c} is the greatest.")