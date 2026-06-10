height = float(input("Enter your height in m "))
weight = float(input("Enter your height in kg "))

BMI = weight / (height**2)

print("Your BMI is",BMI)

if BMI <= 18.4:
    print("You are unerweight.")
elif BMI <=24.9:
    print("You are healthy.")
elif BMI <=29.9:
    print("You hare over weight.")
else:
    print("You are obese")