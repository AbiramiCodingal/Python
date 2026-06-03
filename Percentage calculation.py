# Percentage calculation

e = int(input("enter the english mark :"))
m = int(input("enter the math mark :"))
s = int(input("enter the science mark :"))
c = int(input("enter the computer mark :"))

sum = e + m + s + c
per =sum/400 * 100
print("The total mark is ",sum)
print("The percentage is ",per)
