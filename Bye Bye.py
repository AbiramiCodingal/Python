# nested while loop
try:
    flag = True
    while flag:
        n = int(input("enter a number :"))
        while n%2 == 0:
            print("bye")
        print("the number is odd")
        flag = False
except:
    print("error occured")