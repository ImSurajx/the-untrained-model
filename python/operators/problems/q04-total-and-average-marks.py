# a student scored marks in 3 subjects. take all three as input calculate the total and average, and print both using an f-string.
chem = int(input("enter marks of chem: "))
phy = int(input("enter marks of phys: "))
math = int(input("enter marks of math: "))

print(
    f"""
    chem:\t{chem}
    phy:\t{phy}
    math:\t{math}
    avg:\t{((chem + math + phy) / 3):.2f}%   
    """
)