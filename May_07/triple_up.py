def find_3(numbers):
    pattern = []
    index = 0

    if len(numbers) >= 3:
        for i in numbers:
            if index == 0:
                pattern.append(i)
                index += 1
            elif index + 1 != len(numbers):
                previous_num = numbers[index - 1]
                if i > previous_num:
                    pattern.append(i)
                elif i +1 == len(numbers):
                    previous_num = numbers[-1]
                else:
                    pattern.clear()
                index += 1
                if index + 1 == len(numbers):
                    pattern.append(previous_num)
                    break
    print(check_pattern(pattern))


def check_pattern(pattern):
    if len(pattern) >= 3:
        return True
    return False


num_list1 = [-1, 0, 1, 0]
find_3(num_list1)
