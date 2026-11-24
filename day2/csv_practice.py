import csv

total_revenue = 0
with open("day2/customers.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["bill"])
        print(int(row["bill"]))

        total_revenue = total_revenue + int(row["bill"])

print("total revenue is : ",total_revenue)

with open("day2/customers.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[1])