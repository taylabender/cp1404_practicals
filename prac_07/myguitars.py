"""
Estimate time: 30 min
Actual time:
"""



from prac_07.guitar import Guitar
import csv

FILENAME = 'guitars.csv'

guitar = []
def main():

    # Open csv file to read
    with open(FILENAME, 'r', newline='') as in_file:
        in_file.readline()
        reader = csv.reader(in_file)
        for row in reader:
            guitar.append(Guitar(row[0], int(row[1]), int(row[2])))

    # for line in in_file:
    #     parts = line.strip().split(',')
    #     parts[2] = int(parts[2].replace(",", ""))
    #     guitar = Guitar(parts[0], int(parts[1]), (parts[2]))
    #     print(parts[2])
    # in_file.close()
