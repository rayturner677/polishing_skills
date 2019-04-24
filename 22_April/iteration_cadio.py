def find_difference(list):
    high = 0
    low = list[0]
    for i in list:
        if high < i: high = i

        elif low > i:
            low = i
    print(high - low)


def while_loop_find_difference(list_a):
    high = 0
    low = list_a[0]
    count = 0

    while count < len(list_a):
        if high < list_a[count]:
            high = list_a[count]

        elif low > list_a[count]:
            low = list_a[count]
        count += 1

    print(high - low)


components = [15, 153, 73, 738, 352, 64, 90]
find_difference(components)
while_loop_find_difference(components)
