def day1(file):
    max_calories = []
    temp = []
    with open(file, "r") as f:
        for line in f:
            if line == "\n":
                max_calories.append(sum(temp))
                temp = []
            else:
                temp.append(int(line))
    max_calories.append(sum(temp))
    temp = []
    max_cal = (max(max_calories))
    print("Max calories for one elf: {}".format(max_cal))
    for i in range(3):
        max_cal = (max(max_calories))
        max_calories.remove(max_cal)
        temp.append(max_cal)
    print("Max calories for top 3 elves: {}".format(sum(temp)))

day1("day1.txt")