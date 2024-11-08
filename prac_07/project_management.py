"""
Estimate time: 45min
Actual time:
"""

from prac_07.project import Project
from datetime import datetime

FILENAME = 'projects.txt'

# Display menu
menu = ("(L)oad projects"
        "\n(S)ave projects"
        "\n(D)isplay projects"
        "\n(F)ilter projects by date"
        "\n(A)dd new project"
        "\n(U)pdate project"
        "\n(Q)uit")


def main():
    projects = []

    # Load file
    with open(FILENAME, 'r') as in_file:
        in_file.readline()
        for row in in_file:
            row = row.split("\t")
            projects.append(Project(row[0], row[1], int(row[2]), float(row[3]), int(row[4])))
    
    print(menu)
    choice = input("<<<").upper()
    while choice != "Q":
        if choice == "L":
            break
        if choice == "S":
            break
        if choice == "D":
            break
        if choice == "F":
            break
        if choice == "A":
            break
        if choice == "U":
            break
        else:
            break


main()
