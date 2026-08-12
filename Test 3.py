student = {"Abirami":95,"shara":87,"lily":75,"rose":86,"daisy":68}
sum = 0
for value in student.values():
    sum = sum + value
avg = sum / len(student)
print("the class average is",avg)
print("the max ",max(student.values()))
print("the min ",min(student.values()))
print(student.get("Abirami"))