"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
            "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

for short_state_name, long_state_name in CODE_TO_NAME.items():
    print(f"{short_state_name:3} is {long_state_name}")

print("-------------------")

state_code = input("\nEnter short state: ").upper() # Convert input to uppercase
while True:
    try:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

