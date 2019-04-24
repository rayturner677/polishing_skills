def find_under_sealevel(arr):
    sealevel = 0
    count = 0
    above_sealevel = True

    for i in arr:
        if i < sealevel:
            above_sealevel = False

        elif above_sealevel == False:
            if i > sealevel:
                count += 1
                above_sealevel = True

        else:
            above_sealevel

    print(count)


example = [1, 0, -1, -2, 1, 0, 1, 0]
example2 = [1, -2, 2, -2, 2, -2, 2, 0, 1]
find_under_sealevel(example)
find_under_sealevel(example2)
