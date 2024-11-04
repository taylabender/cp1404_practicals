
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# Part a
for i in range(0, 101, 20):
    print(i, end=' ')
print()

# Part b
for i in reversed(range(1, 20, 1)):
    print(i, end=' ')
print()

# Part c
user_picks = int(input("How many stars? "))
print("*" * user_picks)

# Part d
for i in range(1, user_picks+1):
    print('*' * i)
