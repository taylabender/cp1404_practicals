"""
Estimate time: 45min
Actual time:
"""

from prac_07.project import Project
from datetime import datetime

PROJECT_FILENAME = 'projects.txt'

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
    projects = load_project_data(PROJECT_FILENAME, projects)
    print(menu)
    choice = input(">> ").upper()

    while choice != "Q":
        if choice == "L":
            filename = input("Please enter a filename to load from: ")
            projects = load_project_data(filename, projects)
            # print(projects)

        if choice == "S":
            break

        if choice == "D":
            """Display incomplete and complete projects without numbered indexing, or all projects with numbered indexing"""
            print("Incomplete projects: ")
            for project in sorted(projects):
                if not project.is_complete():
                    print(f"  {project}")

            print("Complete projects: ")
            for project in sorted(projects):
                if project.is_complete():
                    print(f"  {project}")

        if choice == "F":
            break
        if choice == "A":
            break
        if choice == "U":
            break
        else:
            break


def load_project_data(filename, projects):
    # Load file
    try:
        with open(filename, 'r') as in_file:
            in_file.readline()
            for row in in_file:
                row = row.split("\t")
                projects.append(Project(row[0], row[1], int(row[2]), float(row[3]), int(row[4])))
    except FileNotFoundError:
        print("File not found.")
    return projects



main()
