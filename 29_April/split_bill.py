the_bill = [9.50, 11.00, 8.25, 8, 9]
allegy = 1
money_gave = 40


def split_bill(bill, index, partners_money_given):
    first_total = 0

    for i in bill:
        first_total += i

    total = first_total - bill[index]
    value = total / 2
    print(partners_money_given - value)

split_bill(the_bill, allegy, money_gave)
# split_bill([2,4,5,3], 3, 13) => 5.5
