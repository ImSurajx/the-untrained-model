# take two numbers as input. without using * calculate and print their product using += in a way that adds the first number to itself the second number of times.
a = int(input("enter first number: "))
b = int(input("enter second number: "))

result = 0

for _ in range(b):
    result += a

print(f"the output is: {result}")
