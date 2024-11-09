"""
Estimate time: 45min
Actual time: Probably 60-90min. Done over two days.
"""

from prac_07.project import Project
from datetime import datetime
from operator import attrgetter


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
    choice = input("-> ").upper()

    while choice != "Q":
        if choice == "L":
            filename = input("Please enter a filename to load from: ")
            projects = load_project_data(filename, projects)
        elif choice == "S":
            filename = input("Please enter a filename to save to: ")
            save_project(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_dates(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Not a valid choice")

        print(menu)
        choice = input(">> ").upper()
    save_project(PROJECT_FILENAME, projects)
    print("Thanks for using this project manager!")


def update_project(projects):
    """ Update current projects"""
    display_projects(projects)
    for i, project in enumerate(projects):
        print(f"{i}   {project}")
    select_project = int(input("Select a project: "))
    print(projects[select_project])
    percentage = int(input("New percentage: "))
    if percentage != "":
        projects[select_project].percentage = percentage
    priority = int(input("New priority: "))
    if priority != "":
        projects[select_project].priority = int(priority)


def filter_projects_by_dates(projects):
    """ Filter projects by chosen date """
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    start_date = datetime.strptime(date_string, "%d/%m/%Y").date()
    for project in sorted(projects, key=attrgetter("start_date")):
        if project.start_date >= start_date:
            print(f"   {project}")


def save_project(filename, projects):
    """ Save projects to file"""
    with open(filename, "w") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percent", file=out_file)
        for project in projects:
            print(
                f'{project.project}\t{project.start_date.strftime("%d/%m/%Y")}\t{project.priority}\t{project.cost}\t{project.percentage}',
                file=out_file)


def display_projects(projects):
    """Display incomplete and complete projects without numbered indexing. """
    print("Incomplete projects: ")
    for project in sorted(projects):
        if not project.is_complete():
            print(f"  {project}")
    print("Complete projects: ")
    for project in sorted(projects):
        if project.is_complete():
            print(f"  {project}")


def add_project(projects):
    """ Add project to projects list."""
    print("Let's add a new project")
    project_name = input("Name of project: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost = int(input("Cost estimate: "))
    percent = int(input("Percent complete: "))
    projects.append(Project(project_name, start_date, priority, cost, percent))
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
