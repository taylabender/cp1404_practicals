"""
Converting password to stars
"""

MIN_LENGTH = 8


def main():
    password = get_password(MIN_LENGTH)
    print_password(password)


def get_password(min_length):
    """ Get password from user """
    password = input(f"Enter your password with {min_length} characters or more: ")
    while len(password) < min_length:
        print("Invalid password")
        password = input(f"Enter your password with {min_length} characters or more: ")

    return password


def print_password(password):
    """ print password using asterisks with the same amount of characters """
    print('*' * len(password))


main()
