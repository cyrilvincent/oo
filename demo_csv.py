import csv

with open("data/house/house.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(float(row["loyer"]) / float(row["surface"]))