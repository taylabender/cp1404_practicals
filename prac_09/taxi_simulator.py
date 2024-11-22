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
    taxi = [Taxi("Prius", 100, 1.23), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU_LIST)


    choice = input(">>").upper()
    while choice != "Q":
        if choice == "C":
            print("Taxi's available: ")
            for i, taxi in enumerate(taxi):
                print(f"{i} - {taxi}")
        try:
            chosen_taxi = int(input("Choose taxi: "))
            current_taxi = taxi[chosen_taxi]
        except ValueError:
            print("Not a valid number")
        except IndexError:
            print("Invalid option")

        if choice == "D":
            if current_taxi is None:
                print("You need to choose a taxi before you drive")
            else:
                distance = float(input("Drive how far?"))
                current_taxi.start_fare()
                current_taxi.drive(distance)
                cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you: ${cost:.2f}")
                current_bill += cost
        else:
            print("Invalid option")
        print(f"Bill to date: ${current_bill:.2f}")
        print("Taxis are now:")
        for i, taxi in enumerate(taxi):
            print(f"{i} - {taxi}")


main()