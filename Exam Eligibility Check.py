# Medical cause or not
mc = input("enter the student have meddical cause or not(y/n)")
if mc.lower() == 'n':
    att = float(input("enter the attendance percentage : "))
    if att > 75:
        print("The student is allowed to enter the exam ")
    else:
        print("The student is not allowed to write the exam ")
elif mc.lower() == 'y':
    print("the student is allowed to write the exam")
else:
    print("Invalid input")