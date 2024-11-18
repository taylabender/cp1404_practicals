"""
menu:
- G Get valid score (Must be 0-100 inclusive)
- P Print result
- S Show stars
"""

import random


menu = """(G)et valid score (Must be 0-100 inclusive)
(P)rint result
(S)how stars """

def main():
    score = ""
    print(menu)
    choice = input("<<< ").upper()
    while choice != "Q":
        if choice == "G":
            score = int(input("Enter score: "))
        elif choice == "P":
            determine_results(score)
            print(determine_results)
        elif choice == "S":
            print_stars(score)
        else:
            print("invalid choice")
        print("Menu: ")
        choice = input("< ").upper()
    print("Bye bye")


def print_stars(score):
    """ Print stars """
    for i in range(1, score):
        print('*' * i)


def determine_results(score):
    """ determine the grade by score """
    if score > 100 or score < 0:
        print("Invalid")
    elif score < 49:
        print("Bad")
    elif score < 89:
        print("passable")
    elif score <= 100:
        print("Excellent")


main()

