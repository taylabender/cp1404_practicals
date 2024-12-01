"""
Prac 10
"""

import wikipedia

internet_search = input("Enter page title: ")
while internet_search != "":
    results = wikipedia.page(internet_search)
    print(results.title)
    print(results.summary)
    print(results.url)
    internet_search = input("Enter page title: ")

print("Thank you!")

