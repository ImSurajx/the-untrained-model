# logical operators: logical operators are used to combine multiple conditions together
# and -> both conditions -> both are true
# or  -> either condition -> at least one is true
# not -> opposite -> orginal is false.

# AND or NOT
chem = 45
phy = 32

# print true if pass in both subject
print(chem > 33 and phy > 33)

# print true if pass in any subject
print(chem > 33 or phy > 33)

# print true -> false, false -> true
print(not chem > 33)

