import csv

with open('bonus/my_csv.csv', mode='r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print (lines)

print ('----------------------------------')

with open('bonus/my_csv.csv', mode='r') as file:
    csvFile = csv.DictReader(file)
    for lines in csvFile:
        print(lines)

print ('----------------------------------')

rows = []

with open('bonus/my_csv.csv', mode='r') as file:
    csvFile = csv.reader(file)
    header = next(csvFile)
    for lines in csvFile:
        rows .append (lines)

for row in rows:
    print(row)

