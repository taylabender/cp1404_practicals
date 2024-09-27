"""
 Converting password to stars
"""

MIN_LENGTH = 8

while True:
    password = input("Enter your password: ")
    if len(password) >= MIN_LENGTH:
        break
    else:
        print(f"Password must be at least {MIN_LENGTH} characters long. Please try again.")

# Print asterisks for the length of the password
print("*" * len(password))
