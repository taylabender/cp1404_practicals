"""
Prac 10
"""

import wikipedia

internet_search = input("Search Wikipedia: ")
while internet_search != "":
    results = wikipedia.page(internet_search)
    print(results.title)
    internet_search = input("Search Wikipedia: ")

