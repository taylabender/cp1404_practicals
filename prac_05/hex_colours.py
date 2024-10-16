"""
program to look up hexadecimal colours
"""

CODE_TO_COLOUR = {"#00ffff": "aqua", "#ffbf00": "amber", "#fbceb1": "apricot",
                "#89cff0": "babyblue", "3ffee135": "bananayellow", "#ff7f50": "coral",
                "#fffdd0": "cream", "350c878": "emerald", "#4b0082": "indigo"}

colour_code = list(CODE_TO_COLOUR.keys())
colour_name = list(CODE_TO_COLOUR.values())
for colour_code, colour_name in CODE_TO_COLOUR.items():
    print(f"{colour_name}")

print("-------------------")
print("Please enter colour to look up hexadecimal code")

while colour_name != CODE_TO_COLOUR:
    get_colour_name = input("\nEnter colour name here: ").strip().lower()
    if get_colour_name in CODE_TO_COLOUR:
         print(get_colour_name, "is", CODE_TO_COLOUR[colour_code])
    else:
        print(get_colour_name, "is not in the database.")


