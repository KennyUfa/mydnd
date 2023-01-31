import csv

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12]
y=0
with open('../dnd/migrations/spells.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

    print(x,'-----',y)