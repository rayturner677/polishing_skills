#back at python


def find_even_or_odd1():
    user_input = input("Enter positive number: ")
    num = int(user_input)

    print("x: " + num)
    for i in range(num):
        if num % 2 == 0:
            print(str(num) + ' is even!')
        else:
            print(str(num) + ' is odd!')


def find_even_or_odd2():
    user_input = input("Enter positive number: ")
    num = int(user_input)

    print("x: " + user_input)
    while num > 0:
        num -= 1
        if num % 2 == 0:
            print(str(num) + ' is even!')
        else:
            print(str(num) + ' is odd!')


find_even_or_odd2()
