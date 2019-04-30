from collections import Counter


def make_ranson():
    magazine = input("Magazine equal: ")
    user_side_input = input("Note equal: ")
    note = []

    counter = Counter(magazine)
    for char in user_side_input:
        if char in counter:
            counter[char] -= 1
            note.append(counter[char])

    print_if_valid(counter, note)
    return note


def print_if_valid(counter, note):
    for i in note:
        if counter[i] > 0:
            print("Yes, this note is valid.")
    print("NO, this note is invalid.(Try Again)")


make_ranson()
