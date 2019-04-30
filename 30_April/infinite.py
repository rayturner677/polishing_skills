from collections import Counter


def find_a(pattern, count):
    a = pattern.count('a')
    p = int(count / len(pattern))
    remainder = count % len(pattern)
    new_a = pattern[0:remainder - 1]
    total = (a * p) + new_a.count('a')

    print("a" * total)


find_a('abb', 7)
# print(find_a('a', 45), 45)
# print(find_a('abb', 9), 3)
