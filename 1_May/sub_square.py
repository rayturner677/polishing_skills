lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def find_sum(list):
    sub_1 = list[0][:2]
    sub_2 = list[0][1:3]
    sub_3 = list[1][:2]
    sub_4 = list[1][1:3]
    sub_5 = list[1][:2]
    sub_6 = list[1][1:3]
    sub_7 = list[2][:2]
    sub_8 = list[2][1:3]

    print(sub_1, sub_2)
    print(sub_3, sub_4)
    print(sub_5, sub_6)
    print(sub_7, sub_8)

    sum1 = sum(sub_1) + sum(sub_3)
    sum2 = sum(sub_2) + sum(sub_4)
    sum3 = sum(sub_5) + sum(sub_7)
    sum4 = sum(sub_6) + sum(sub_8)

    print(sum1, sum2)
    print(sum3, sum4)

    grand_total = sum1 + sum2 + sum3 + sum4

    print(grand_total)


find_sum(lst)
