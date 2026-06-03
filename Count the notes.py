# denomenation calculation
amt = int(input("enter the amout"))
note500 = amt//500
note100 = (amt%500)//100
note50 = ((amt%500)%100)//50
print("The no of 500 rupee note",note500)
print("The no of 100 rupee note",note100)
print("The no of 50 rupee note",note50)