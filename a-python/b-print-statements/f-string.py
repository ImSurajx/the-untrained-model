# f-string:  lets you embed variables values directly inside a string. put an f-before the opening quote and write variables inside {}.

name = "Suraj Kumar"
age = 22
course = "Python"

# without f-string (messy)
print("Hello, " + name + ". You are " + str(age) + " years old.")

# with f-string (clean and readable)
print(f"Hello, {name}. You are {age} years old.")
print(f"Welcome to the {course} course!")

# simple math inside {}
price = 499
qty = 3
print(f"Total: {price * qty}")
