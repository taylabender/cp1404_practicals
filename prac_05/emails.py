"""
Program to store users' email addresses into a dictionary.
Estimate time: 30 minutes
Actual time:
"""
def main():
    name_from_email = {}
    email = input("Enter your email address: ")

    while True:
        suggested_name = get_name_from_email(email)
        confirmation = input(f"Is your name {suggested_name}? (Y/N) ")

        if confirmation.upper() != "Y":
            name = input("Enter your name: ")
            print(f"{name}'s email address is {email}")
        else:
            name_from_email[email] = suggested_name  # Store the suggested name

        for email, name in name_from_email.items():
            print(f"{name}'s email address is {email}")


def get_name_from_email(email):
    username = email.split('@')[0]
    parts = username.split('.')
    suggested_name = " ".join(parts).title()
    return suggested_name


main()

# tayla.bender@outlook.com