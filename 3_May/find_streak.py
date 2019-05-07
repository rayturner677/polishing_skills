def find_streak(num_list):
    streak = []
    streak2 = []
    size = 0
    i = 0

    for num in num_list:
        streak.append(num)
        if num == streak[0] and num == num_list[i + 1]:
            streak.append(num)
            streak.remove(num)

        elif size > len(streak):
            streak.clear()

        
        size = len(streak)
        i += 1
    print(streak)


this_list = [1, 1, 2, 2, 2, 7, 7, 8, 8, 9, 9]
find_streak(this_list)
