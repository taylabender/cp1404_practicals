"""
The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the screen.

"""
# Ask user for the number of items
item_count = int(input("Number of items? "))

# Invalid number of items
while item_count < 0:
    print("Invalid number")
    item_count = int(input("Number of items? "))

# cost per item
total = 0
for i in range(item_count):
    price = float(input("Item cost: "))
    total += price

# discount of 10% for shop < $100
    if total <= 100:
        discount = total * 0.1
        total = total - discount

print(f"Total price for {item_count} is {total}")

