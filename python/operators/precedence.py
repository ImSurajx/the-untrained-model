# when multiple operator are in one expression, python follows a specific order just like BODMAS in maths
# order (highest to lowest)
# ** -> exponetiation -> *,/,//,% -> multiplication & division -> +,- -> addition & subtraction

# without knowing precedence, this looks confusing 
print(2 + 3 * 4) # 14 not 20
print(10-2**3) # 2 not 512
print(10 // 2 + 3) # 8 not 1

# use parentheses to force the order you want
print((2+3) * 4) # 20
print((10-2)**3) # 512
