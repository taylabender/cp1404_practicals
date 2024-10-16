"""
program to look up hexadecimal colours
"""

CODE_TO_NAME = {"#00ffff": "Aqua", "#ffbf00": "Amber", "#fbceb1": "Apricot",
                "#89cff0": "Baby Blue", "3ffee135": "Banana Yellow", "#ff7f50": "Coral",
                "#fffdd0": "Cream", "350c878": "Emerald", "#4b0082": "Indigo"}

colour_code = list(CODE_TO_NAME.keys())
colour_name = list(CODE_TO_NAME.values())
max_length = max(len(colour_name) for colour_name in list(CODE_TO_NAME.values()))
for colour_code, colour_name in CODE_TO_NAME.items():
    print(f"{colour_name:{max_length}} is {colour_code}")

