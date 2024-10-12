"""
Lottery ticket generator
"""
import random
columns = 6


quick_pick = int(input("Enter the number of quick picks: "))
if quick_pick <= 0:
       print("Invalid number, please enter positive number")
else:
       for i in range(quick_pick):
              quick_pick =[]

# while len(numbers) < quick_pick:
#       for i in range(quick_pick):
#             quick_pick = g


