from prac_06.guitar import Guitar

def main():
    print("My guitars!")
    guitars = []

    # Get guitar details from user
    name = input("Guitar Name: ")
    while name != "":
        add_guitar = get_user_input(guitars, name)
        print(f"{add_guitar.name} ({add_guitar.year}) : ${add_guitar.cost} added.")
        name = input(f"\nGuitar Name: ")

    if guitars:
        print("\nThese are my guitars:")


def get_user_input(guitars, name):
    year = int(input("Enter a year: "))
    cost = float(input("Enter a cost: "))
    add_guitar = Guitar(name, year, cost)
    guitars.append(add_guitar)
    return add_guitar


main()