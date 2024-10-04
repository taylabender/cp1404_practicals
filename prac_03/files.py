"""
Do from scratch exercise.
"""


# Task 1
FILENAME = 'task_01'
out_file = open(FILENAME, 'w')
name = input('What is your name? ')
print(name, file=out_file)
out_file.close()

# Task 2
in_file = open('task_01', 'r')
for line in in_file:
    print(f"Hello {line}")
in_file.close()

# Task 3
with open("numbers.txt", "r") as out_file_numbers:
    lines = out_file_numbers.readlines()
    a = int(lines[0].strip())
    b = int(lines[1].strip())
    c = (a + b)
    print(f"{a} + {b} = {c}")

# Task 4
total = 0
with open("numbers.txt", "r") as out_file_numbers_02:
    for line in out_file_numbers_02:
        numbers = int(line.strip())
        total += numbers
print(f"The sum of all numbers in numbers.txt is {total}")




