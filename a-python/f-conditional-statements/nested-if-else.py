# you can place an if statement inside another if statment. this is called nesting and is useful when a second condition only makees sense if the first one is already true.

age = 19
has_degree = False

if age >= 18:
    print("age requirement met.")
    if has_degree:
        print("you are eligble for this job.")
    else:
        print("you need a degree for this job.")
else:
    print("your are too young to apply")

# pass: pass the code block for the future conditions.