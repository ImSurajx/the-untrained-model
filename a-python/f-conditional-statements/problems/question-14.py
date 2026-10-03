# a shop gives discounts based on purchase amount
"""
above 5000 -> 20% discount
above 2000 -> 10% discount
above 1000 -> 5% discount
1000 or below -> no discount
"""
purchase_amount = int(input("enter amount: "))
amount = None
if purchase_amount > 5000:
    amount = purchase_amount - (purchase_amount * 20)/100
    print(f"congrates! you got discount of 20%, you just have to pay: {amount}")
elif purchase_amount > 2000:
    amount = purchase_amount - (purchase_amount * 10)/100
    print(f"congrates! you got discount of 10%, you just have to pay: {amount}")
elif purchase_amount > 1000:
    amount = purchase_amount - (purchase_amount * 5)/100
    print(f"congrates! you got discount of 5%, you just have to pay: {amount}")
elif purchase_amount <= 1000 and purchase_amount >= 0:
    amount = purchase_amount
    print(f"you just have to pay: {amount}")