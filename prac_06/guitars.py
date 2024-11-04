from prac_06 import guitar
from prac_06.guitar import Guitar

def main():
    print("My guitars!")
    guitars = []

    # # Test data
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    # guitars.append(Guitar("Fender Stratocaster", 2014, 765.4))


    # Get guitar details from user
    name = input("Guitar Name: ")
    while name != "":
        add_guitar = get_user_input(guitars, name)
        print(f"{add_guitar.name} ({add_guitar.year}) : ${add_guitar.cost} added.")
        name = input(f"\nGuitar Name: ")

    # Display guitars
    if guitars:
        print("\nThese are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage = "(Vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year:>4}), worth $ {guitar.cost:>9,.2f} {vintage}")

def get_user_input(guitars, name):
    """ Get user input to add guitar. """
    year = int(input("Enter a year: "))
    cost = float(input("Enter a cost: "))
    add_guitar = Guitar(name, year, cost)
    guitars.append(add_guitar)
    return add_guitar


main()