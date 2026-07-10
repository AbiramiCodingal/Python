# Tip, the waiter
def tip(amt,per):
    wtip = amt*per/100
    print("The amt : ",amt)
    print("Waiter tip",wtip)
    print("total amt",amt+wtip)

amt = float(input("Enter the amt"))
tip(amt,2)