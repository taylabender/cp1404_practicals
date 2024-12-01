"""
Prac 10
"""

import wikipedia

internet_search = input("Enter page title: ")
while internet_search != "":
    try:
        results = wikipedia.page(internet_search)
        print(results.title)
        print(results.summary)
        print(results.url)
        internet_search = input("Enter page title: ")

    except wikipedia.DisambiguationError as limit:
        print(f"We need a more specific title. Try one of the following, or enter a new search. ")
        for option in limit.options[:10]:
            print(option)
        internet_search = input("Enter page title: ")

    except wikipedia.PageError:
        print(f"We couldn't find the page {internet_search}")
        internet_search = input("Enter page title: ")

print("Thank you!")

