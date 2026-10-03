# take a number as input. using the ternary operator, print "even" or "odd" in a single line
num = int(input("enter a number: "))
print(f"{num} is even.") if num % 2 == 0 else print(f"{num} is odd.")