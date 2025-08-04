import csv
with open("Task day2\ people.csv","r") as file:
    read=csv.reader(file)
    for r in read:
        print(r)


# output
# ['name', 'age', 'gender']
# ['Deepak', '25', 'm']
# ['Gayatri', '22', 'f']
# ['chinmaya', '29', 'm']