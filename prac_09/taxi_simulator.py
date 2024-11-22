"""
Prac 09 - taxi simulator
"""
from http.cookiejar import uppercase_escaped_char

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

menu_list = ("q)uit, "
            "c)hoose taxi, "
             "d)rive")
print(menu_list)

choice = input(">>").upper()
while choice != "Q":
    if choice == "C":
        break
    if choice == "D":
        break
    else:
        break
# display menu
# get choice
# while choice != <quit option>
#     if choice == <first option>
#         <do first task>
#     else if choice == <second option>
#         <do second task>
#     ...
#     else if choice == <n-th option>
#         <do n-th task>
#     else
#         display invalid input error message
#     display menu
#     get choice
# <do final thing, if needed>