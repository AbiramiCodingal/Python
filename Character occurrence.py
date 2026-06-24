# Character occurrence

str1 = input("Enter a phrase : ")
ch = input("enter a character : ")
count = 0 
for i in str1:
    if i == ch:
        count = count + 1

print(f"the number of occurrence of {ch} in {str1} is {count}")