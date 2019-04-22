def getOutput():
    word = input("Enter: ")
    for char in word:
        position = ord(char) - ord("a") + 1
        print(char * position)


def get_newOutput():
    word = input("Enter: ")
    i = 0
    char = word[i]

    while len(word) > i:
        position = ord(char) - ord("a") + 1
        print(char * position)
        i += 1


getOutput()
get_newOutput()
