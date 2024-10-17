"""
Estimate: 25 minutes
Actual:
"""

sentence = input("Enter a sentence: ")
word_count = {}

for word in sentence.lower().split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


