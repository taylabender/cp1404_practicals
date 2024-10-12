"""
Lottery ticket generator
"""
import random
NUMBERS_PER_LINE = 6


try:
       number_of_quick_pick = int(input("Enter the number of quick picks: "))
       if number_of_quick_pick < 0:
              print("Invalid number, please enter positive number")
              number_of_quick_pick = int(input("Enter the number of quick picks: "))

       for i in range(number_of_quick_pick):
              quick_pick =[]
              for j in range(NUMBERS_PER_LINE):
                     number = random.randint(1, 45)
                     while number in quick_pick:
                            number = random.randint(1, 45)
                     quick_pick.append(number)
              quick_pick.sort()
              print(" ".join(f"{number:2d}" for number in quick_pick))

except ValueError:
       print("Invalid input.")

