# take a number as input. print the result of that number raised to the power of 3 using **. also print what // 7 and % 7 give for the same number.

num = int(input("enter a number: "))
print(
    f"""
    exponention:\t{num ** 3}
    floor division:\t{num // 7}
    remainder:\t{num ** 3}
    """
)