from collections import Counter

def most_frequent(s):
    frequency = Counter(s)
    sorted_frequency = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=False))
    for letter, count in sorted_frequency.items():
        print(letter, count)

most_frequent("mississippi")