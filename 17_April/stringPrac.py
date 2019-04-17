string1 = input("Enter:")
string2 = input("Enter:")

nw_string1 = []


def sortFunction():
    if string1 > string2:
        newString(string1, string2)
    else:
        newString2(string1, string2)


def newString(string1, string2):
    for i in string1 or i == ".":
        if i in string2:
            nw_string1.append(i)
            print(i)
        else:
            string1.replace(i, ".")
            nw_string1.append(".")
    print(nw_string1)


def newString2(string1, string2):
    for i in string2 or i == ".":
        if i in string1:
            nw_string1.append(i)
            print(i)
        else:
            string1.replace(i, ".")
            nw_string1.append(".")

    print(nw_string1)


sortFunction()
