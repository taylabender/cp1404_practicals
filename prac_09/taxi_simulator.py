"""
Prac 09 - taxi simulator
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU_LIST = ("q)uit, "
            "c)hoose taxi, "
             "d)rive")


def main():
    current_taxi = None
    current_bill = 0.0
    taxis = [Taxi("Prius", 100, 1.23), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU_LIST)


    choice = input(">>").upper()
    while choice != "Q":
        if choice == "C":
            current_taxi = choose_taxi(current_taxi, taxis)
        elif choice == "D":
            current_bill = drive_taxi(current_bill, current_taxi)
        else:
            print("Invalid option")
        print(f"Bill to date: ${current_bill:.2f}")
        print(MENU_LIST)
        choice = input(">>").upper()

    print(f"Bill to date: ${current_bill:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def drive_taxi(current_bill, current_taxi):
    if current_taxi is None:
        print("You need to choose a taxi before you drive")
    else:
        try:
            distance = float(input("Drive how far?"))
            current_taxi.start_fare()
            current_taxi.drive(distance)
            cost = current_taxi.get_fare()
            print(f"Your {current_taxi.name} trip cost you: ${cost:.2f}")
            current_bill += cost
        except ValueError:
            print("Not a valid number")
    return current_bill


def choose_taxi(current_taxi, taxis):
    print("Taxis available: ")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    try:
        chosen_taxi = int(input("Choose taxi: "))
        current_taxi = taxis[chosen_taxi]
    except ValueError:
        print("Not a valid number!")
    except IndexError:
        print("Invalid option!")
    return current_taxi


main()