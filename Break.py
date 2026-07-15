# checking alphabet "a" or "A" in a phrase

phrase = input("enter the phrase : ")

for i in phrase:
    if i.lower() == "a":
        print(f"alphabet 'a' or alphabet 'A' is present in '{phrase}'")
        break
else:
    print(f"alphabet 'a' or alphabet 'A' is not present in '{phrase}'")