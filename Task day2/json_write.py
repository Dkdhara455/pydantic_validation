import json
data={
    "name":"Deepak",
    "age":25,
    "city":"surat",
    "skils":["python","databse","django"]
}
with open("Task day2\ data.json","w") as file:
    json.dump(data,file,indent=4)