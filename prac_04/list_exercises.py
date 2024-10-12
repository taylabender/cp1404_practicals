"""
Prompt the user for 5 numbers and then store
each of these in a list called 'numbers'.
"""

numbers = []

def main():

    print("Enter 5 numbers below")
    get_number()
    average = sum(numbers) / len(numbers)
    print_list(average)


def print_list(average):
    """ Print output information about the numbers. """
    print(f"The first number is {numbers[0]:.0f}")
    print(f"The last number is {numbers[-1]:.0f}")
    print(f"The smallest number is {min(numbers):.0f}")
    print(f"The largest number is {max(numbers):.0f}")
    print(f"The average of the numbers is {average:.1f}")


def get_number():
    """ Get numbers from user """
    for i in range(5):
        number = float(input(f"Number {i + 1}: "))
        numbers.append(number)


main()