"""
One very common programming task is to make menus by combining looping
(repeat the program until the user quits) with selection (let
the user decide what to do).
"""
# get name
# display menu
# get choice
# while choice != Q
#    if choice == H
#        display "hello" name
#    else if choice == G
#        display "goodbye" name
#    else
#        display invalid message
#    display menu
#    get choice
# display finished message
# Display menu
menu_list = "(h)ello\n(g)oodbye\n(q)uit"
name = input("Enter name? ")
print(menu_list)

# menu list
choice = input("<<<").upper()
while choice != "Q":
    if choice == "H":
        print("hello", name)
        break
    elif choice == "G":
        print("goodbye", name)
        break
    else:
        print("Invalid key")
        print(menu_list)
        choice = input("<<<").upper()
if choice == "Q":
    print("Quitting program, goodbye for reals")

