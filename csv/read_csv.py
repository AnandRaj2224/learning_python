# csv ---> comma seperated values
#          they are common file format for tabular data

# reading from csv file
from csv import reader
with open("fighters.csv") as file:
    csv_reader = reader(file)
    for row in csv_reader:
        print(row)