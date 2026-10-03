# take a person's age and whether they have a valid ID (true/false) as input. they can enter a venue only if they are 18 or older and have a valid ID. print the appropriate message

age = int(input("enter your age: "))
valid_id = bool(int(input("do you have a valid id card enter (0-false/1-true): ")))

if age >= 18:
    print("you have a valid age.")
    if valid_id:
        print("you can enter the venue.")
    else:
        print("but you can't enter the venue please get a valid id.")
else:
    print("you are too young to enter the venue.")