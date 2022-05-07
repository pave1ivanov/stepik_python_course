import csv

counter = {}
with open("Crimes.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[5] not in counter:
            counter[row[5]] = 1
        else:
            counter[row[5]] += 1

biggest_crime = ""
biggest_crime_count = 0
for crime in counter:
    if counter[crime] > biggest_crime_count:
        biggest_crime = crime
        biggest_crime_count = counter[crime]

print(biggest_crime)