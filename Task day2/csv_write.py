import csv
data=[
    ["name","age","gender"],
    ["Deepak",25,"m"],
    ["Gayatri",22,"f"],
    ["chinmaya",29,"m"]
]
with open("Task day2\ people.csv",'w',newline='') as file:
    writer=csv.writer(file)
    writer.writerows(data)