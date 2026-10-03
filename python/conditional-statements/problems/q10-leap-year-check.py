# take a year as input. check if it is leap year. a leap is a leap year if it divisible by 4 but not by 100 unless it is also divisible by 400

year = int(input("enter the year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
