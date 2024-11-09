"""
Estimate time: 45min
Actual time:
"""

from prac_07.project import Project
from datetime import datetime

PROJECT_FILENAME = 'projects.txt'

# Display menu
menu = ("- (L)oad projects"
        "\n- (S)ave projects"
        "\n- (D)isplay projects"
        "\n- (F)ilter projects by date"
        "\n- (A)dd new project"
        "\n- (U)pdate project"
        "\n- (Q)uit")


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
            for i, project in enumerate(projects):
                print(f"{i}   {project}")

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
            projects = add_project(projects)

        if choice == "U":
            break
        else:
            # print("Not a valid choice")
            break
    # print(menu)
    # choice = input(">> ").upper()
    # print("Thanks for using this project manager!")


def add_project(projects):
    print("Let's add a new project")
    project = input("Name of project: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost = int(input("Cost estimate: "))
    percent = int(input("Percent complete: "))
    projects.append(Project(project, start_date, priority, cost, percent))
    return projects

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
