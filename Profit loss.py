actual_cost = float(input("please Enter the Actual Product Price: "))
sale_amount = float(input("please Enter the sale Amount:"))
if sale_amount > actual_cost:
    amount = sale_amount - actual_cost 
    print (amount,"is a profit")
else:
    print("It is a loss")    