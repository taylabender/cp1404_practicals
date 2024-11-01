from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Another Guitar", 2013, 1512.9)

print(f"{gibson.name} get_age() - Expected 100. Got {gibson.get_age()}")
print(f"{guitar2.name} get_age() - Expected 9. Got {guitar2.get_age()}")
