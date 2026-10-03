# python lets you write a simple if-else in a single line. this is called the ternary operator. it is useful when you want to assign a value based on a condition.

# normal way
age = 16
if age >= 18:
    status = "Adult"
else: 
    status = "Minor"
print(status)

# shorthand way (same result, one line)
age = 45
status = "Adult" if age >= 18 else "Minor"
print(status)