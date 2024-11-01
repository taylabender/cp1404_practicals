from prac_06.guitar import Guitar

def main():
    print("My guitars!")
    guitar = []

    name = input("Guitar Name: ")
    if name == "":
        break

    year = int(input("Enter a year: "))
    cost = float(input("Enter a cost: "))
    add_guitar = Guitar(name, year, cost)
    guitar.append(Guitar(year, cost))

