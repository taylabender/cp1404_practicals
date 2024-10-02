"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
- When an invalid number occurs, e.g. letters.

2. When will a ZeroDivisionError occur?
- When a division by zero occurs.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
- Yes, by adding in a zero check at the beginning of the code.
"""

def main():

    try:
        denominator, numerator = get_fraction()
        if denominator == 0:
            print("The denominator cannot be 0.")
        else:
            fraction = numerator / denominator
            print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    print("Finished.")


def get_fraction():
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    return denominator, numerator


main()