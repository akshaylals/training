import os

os.chdir(os.path.dirname(__file__))

import csv

# Reading csv file
with open('mycsvfile.csv') as f:
    csvreader = csv.reader(f)
    header = next(csvreader)
    rows = [row for row in csvreader]

print(header)
print(rows)


# Without csv module
with open('mycsvfile.csv') as f:
    header = [i.strip() for i in f.readline().split(',')]
    rows = [i.strip().split(',') for i in f.readlines()]

print(header)
print(rows)

# Writing csv file using csv module
with open('mycsvfile2.csv', 'w', newline='') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(['Names', 'Experience', 'Salary'])
    csvwriter.writerows([
        ['Anu', 9, 40000],
        ['Vinu', 8, 30000],
        ['Manu', 5, 25000]
    ])
