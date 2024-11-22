"""
Prac 09 - taxi simulator
"""
from http.cookiejar import uppercase_escaped_char

from pkg_resources import non_empty_lines

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU_LIST = ("q)uit, "
            "c)hoose taxi, "
             "d)rive")


def main():
    current_taxi = None
    current_bill = 0.0
    taxi = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU_LIST)


    choice = input(">>").upper()
    while choice != "Q":
        if choice == "C":
            print("Taxi's available: ")
            for i, taxi in enumerate(taxi):
                print(f"{i} - {taxi}")
            chosen_taxi = int(input("Choose taxi: "))
            current_taxi = taxi[chosen_taxi]

        if choice == "D":
            break
        else:
            break
    # display menu
    # get choice
    # while choice != <quit option>
    #     if choice == <first option>
    #         <do first task>
    #     else if choice == <second option>
    #         <do second task>
    #     ...
    #     else if choice == <n-th option>
    #         <do n-th task>
    #     else
    #         display invalid input error message
    #     display menu
    #     get choice
    # <do final thing, if needed>