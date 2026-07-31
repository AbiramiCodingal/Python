# country code

country = { "India": "0091",
           "qatar":"0974",
           "Pakistan":"0092",
           "Nepal":"0977",
           "USA":"001"}

print("The country code for India is ")
print(country.get("India","not found"))

print("The country code for Australia is ")
print(country.get("Australia","not found"))
