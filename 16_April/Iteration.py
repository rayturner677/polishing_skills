def iteration_prac():
    num_input = input("Enter: ")
    num = int(num_input)
    print("x: ", num)
    for i in range(1, num):
        if num % i == 0:
            print(str(i) + " is a factor of " + str(num))
        else:
            print(str(i) + " is not a factor of " + str(num))


def iteration_prac_while():
    num_input = input("Enter: ")
    num = int(num_input)
    i = num
    print("x: ", num)
    while num > 0:
        if num % i == 0:
            print(str(i) + " is a factor of " + str(num))
        else:
            print(str(i) + " is not a factor of " + str(num))
        i -= 1

iteration_prac_while()
iteration_prac()
