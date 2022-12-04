import string

def day3_part1(file):
    priorities = string.ascii_letters
    priority_sum = 0
    with open(file, "r") as f:
        data = f.readlines()
    for line in data:
        line_len = len(line)
        half_way = int(line_len / 2)
        comp_1 = line[0:half_way]
        comp_2 = line[half_way:line_len]
        for letter in comp_1:
            if letter in comp_2:
                priority_sum += priorities.index(letter) + 1
                break
    print("The sum of priorities: {}".format(priority_sum))

def day3_part2(file):
    priorities = string.ascii_letters
    priority_sum = 0
    with open(file, "r") as f:
        data = f.readlines()
    cur_line = 0
    for line_num in range(int(len(data) / 3)):
        for letter in data[cur_line]:
            if letter in data[cur_line + 1]:
                if letter in data[cur_line + 2]:
                    priority_sum += priorities.index(letter) + 1
                    break
        cur_line += 3
    print("The sum of priorities: {}".format(priority_sum))

day3_part1("day3.txt")
day3_part2("day3.txt")