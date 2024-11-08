from prac_07.guitar import Guitar
import csv

def main():
    guitar = []
    # Open csv file to read
    in_file = open('guitar.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        parts[2] = int(parts[2].replace(",", ""))
        guitar = Guitar(parts[0], int(parts[1]), (parts[2]))
        print(parts[2])
    in_file.close()
