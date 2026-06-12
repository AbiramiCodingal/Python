# Selection of ride
choice = input("1.bike \n2.Car \n enter your choice : ")
if choice == "1":
    ch = input("1.Yamaha \n2.Bullet \n enter your bike choice : ")
    if ch == "1":
        print("you have selected yamaha")
    elif ch == "2":
        print("you have selected bullet")
    else:
        print("invalid input")
elif choice == "2":
    ch = input("1.Toyato \n2.Mercedes \n enter your Car choice : ")
    if ch == "1":
        print("you have selected Toyato")
    elif ch == "2":
        print("you have selected Mercedes")
    else:
        print("invalid input")
else:
    print("invalid input")