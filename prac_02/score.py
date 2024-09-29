"""
Refactoring broken scores to include functions
"""

score = float(input("Enter score: "))
if score > 100 or score < 0:
    print("Invalid")
elif score < 49:
    print("Bad")
elif score < 89:
    print("passable")
elif score <= 100:
    print("Excellent")
