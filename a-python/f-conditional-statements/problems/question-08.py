# take two numbers as input. print the greter of the two. if they are equalm print "Both are equal."
a = int(input("enter first number: "))
b = int(input("enter second number: "))

if a > b:
    print(f"{a} is greater than {b}.")
elif a < b:
    print(f"{b} is greater than {a}.")
elif a == b:
    print(f"{a} & {b}, both are equal.")
