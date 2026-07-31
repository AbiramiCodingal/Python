# Get rid of the duplicates

student = {
    "id1" :{
         "name":"sara",
        "class":11,
        "subject":['English','Maths','Science']
    },
    "id2" :{
             "name":"Raj",
            "class":11,
            "subject":['CS','Maths','Science']
        },
    "id3" :{
             "name":"sara",
            "class":11,
            "subject":['English','Maths','Science']
        },
    "id4" :{
             "name":"Rahim",
            "class":11,
            "subject":['Commerce','Maths','Science']
        }
}

unique_dic = {}
for key,value in student.items():
    if value not in unique_dic.values():
        unique_dic[key] = value

print("After removing duplicates : \n ")
print(unique_dic)