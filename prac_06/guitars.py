from prac_06.guitar import Guitar

def main():
    print("My guitars!")
    guitars = []

    # Get guitar details from user
    name = input("Guitar Name: ")
    while name != "":
        year = int(input("Enter a year: "))
        cost = float(input("Enter a cost: "))
        add_guitar = Guitar(name, year, cost)
        guitars.append(add_guitar)
        print(f"Guitar added: {add_guitar.name}")
        print()



main()