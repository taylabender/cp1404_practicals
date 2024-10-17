"""
Program to store users' email addresses into a dictionary.
Estimate time: 30 minutes
Actual time:
"""

name_from_email = {}
email = input("Enter your email address: ").strip()

username = email.split('@')[0]
parts = username.split('.')
suggested_name = " ".join(parts).title()

confirmation = input(f"Is your name {suggested_name}? (Y/N) ").lower
