import json
with open("Task day2\ data.json","r") as file:
    data=json.load(file) #here data is dictionary
for key,value in data.items():# reading the dictionary in key and value pair
    print(f"{key}--{value}")
# you can read one by one also
print(data["name"]) #o/p-Deepak
print(data["age"]) #o/p-25

# output
# name--Deepak
# age--25
# city--surat
# skils--['python', 'databse', 'django']