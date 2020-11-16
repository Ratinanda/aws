import csv
with open('rati.txt') as csv_file:
     test = csv.reader(csv_file,delimiter="\t")
     name=[(s, r) for r, s in test]
     print(name)

