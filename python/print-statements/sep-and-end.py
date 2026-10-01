# sep and end : by default, print puts a space b/w multiple values and a new line at the end, you can change both using sep and end.

# sep: changes the separator between values
print("2024","01","15",sep="-")
print("a","b","c", sep="|")

# end: changes what is printed at the very end
print("loading", end="....")
print("done")

# combining both
print("10","20","30", sep=",", end="!\n")