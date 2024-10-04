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


