def find_pair(socks):
    singles = []
    pairs = 0

    for sock in socks:
        if sock not in singles:
            singles.append(sock)

        elif sock in singles:
            pairs += 1
            singles.remove(sock)
    print(pairs)


arr1 = ['blue', 'blue', 'yellow', 'green', 'orange', 'purple', 'red', 'black']
arr2 = ['blue', 'purple', 'yellow', 'blue', 'orange', 'purple', 'red', 'black']

# find_pair(arr1)
find_pair(arr2)
