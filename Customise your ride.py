# electricity bill
u = int(input("Enter the units :"))
if u < 50:
    amt = 2.60 * u + 25
elif u < 100:
    amt = 3.25 * u + 35
elif u < 200:
    amt = 5.26 * u + 45
else:
    amt = 8.25 * u + 75
print("the electricity bill amt is Rs.",round(amt,2))

