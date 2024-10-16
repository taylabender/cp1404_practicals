"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
            "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

short_state_name = list(CODE_TO_NAME.keys())
long_state_name = list(CODE_TO_NAME.values())
for short_state_name, long_state_name in CODE_TO_NAME.items():
    print(f"{short_state_name:3} is {long_state_name}")
print("-------------------")

state_code = input("Enter short state: ").upper() #convert input to uppercase
while state_code != "":
   try:
       print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()


