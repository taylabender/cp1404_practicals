"""
Estimate: 25 minutes
Actual:
"""

sentence = input("Enter a sentence: ")
word_count = {}


def main():

    count_words()
    longest_word = max(len(word) for word in word_count.keys())
    sort_and_print(longest_word)


def sort_and_print(longest_word):
    for word in sorted(word_count.keys()):
        print(f"{word:{longest_word}}: {word_count[word]}")


def count_words():
    for word in sentence.lower().split():
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1


main()

