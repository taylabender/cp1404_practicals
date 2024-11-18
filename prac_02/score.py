"""
Refactoring broken scores to include functions
"""
import random

def main():
    """ get score from input """
    score = float(input("Enter score: "))
    determine_grade(score)


def determine_grade(score):
    """ determine grade from score """
    if score > 100 or score < 0:
        print("Invalid")
    elif score < 49:
        print("Bad")
    elif score < 89:
        print("passable")
    elif score <= 100:
        print("Excellent")

random_score = random.randint(0, 100)
determine_grade(random_score)
print(random_score)

main()