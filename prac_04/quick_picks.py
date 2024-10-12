"""
Lottery ticket generator
"""
import random

CONSTANTS = random.randint(1, 45)
quick_pick = int(input("Enter the number of quick picks: "))
rows = quick_pick

for i in range(rows):
       print(quick_pick)


