"""
Estimate time: 30 min
Actual time:
"""

from prac_07.guitar import Guitar
import csv

FILENAME = 'guitars.csv'
guitars = []

def main():
    # Open csv file to read
    with open(FILENAME, 'r', newline='') as in_file:
        in_file.readline()
        reader = csv.reader(in_file)
        for row in reader:
            guitars.append(Guitar(row[0], int(row[1]), float(row[2])))

    # Get input from user
    name = input("Name of guitar: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        name = input("Name of guitar: ")

    # Write to csv file
    with open(FILENAME, 'w') as out_file:
        for guitar in sorted(guitars):
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)
            print(guitar)

main()