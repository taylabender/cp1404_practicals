"""
Estimate time: 45min
Actual time:
"""

from prac_07.project import Project
import csv

FILENAME = 'projects.txt'
projects = []

def main():
    # Open filename
    with open(FILENAME, 'r', newline='') as in_file:
        in_file.readline()
        reader = csv.reader(in_file)
        for row in reader:
            projects.append(Project(row[0], (row[1]), int(row[2]), float(row[3]), int(row[4])))


