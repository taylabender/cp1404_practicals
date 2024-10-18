"""
Program to store users' email addresses into a dictionary.
Estimate time: 30 minutes
Actual time:
"""
def main():


    name_from_email = {}
    email = input("Enter your email address: ")

    while email != "":
        username = email.split('@')[0]
        parts = username.split('.')
        suggested_name = " ".join(parts).title()

        confirmation = input(f"Is your name {suggested_name}? (Y/N) ")
        if confirmation.upper() != "Y":
            name = input("Enter your name: ")
            name_from_email[email] = name # stores the entered name
        else:
            name_from_email[email] = suggested_name # stores the suggested name

        email = input("Enter your email address: ")

    for email, name in name_from_email.items():
        print(f"{name} email address is {email}")

main()


    # name = suggested_name
    # print(f"{name}'s email address is {email}")
# else:
#     name_from_email[email] = suggested_name


# tayla.bender@outlook.com