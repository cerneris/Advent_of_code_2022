def day4_part1(file):
    with open(file, "r") as f:
        data = f.readlines()
    overlap = 0
    for line in data:
        section_1, section_2 = line.split(",")
        section_1_start, section_1_stop = section_1.split("-")
        section_2_start, section_2_stop = section_2.split("-")
        range_1 = range(int(section_1_start), int(section_1_stop) + 1)
        range_2 = range(int(section_2_start), int(section_2_stop) + 1)
        in_range = False
        if len(range_1) >= len(range_2):
            for value in range_2:
                if value in range_1:
                    in_range = True
                else:
                    in_range = False
                    break
        else:
            for value in range_1:
                if value in range_2:
                    in_range = True
                else:
                    in_range = False
                    break
        if in_range:
            overlap += 1
    print("Overlapping sections part 1: {}".format(overlap))

def day4_part2(file):
    with open(file, "r") as f:
        data = f.readlines()
    overlap = 0
    for line in data:
        section_1, section_2 = line.split(",")
        section_1_start, section_1_stop = section_1.split("-")
        section_2_start, section_2_stop = section_2.split("-")
        range_1 = range(int(section_1_start), int(section_1_stop) + 1)
        range_2 = range(int(section_2_start), int(section_2_stop) + 1)
        in_range = False
        if len(range_1) >= len(range_2):
            for value in range_2:
                if value in range_1:
                    in_range = True
                    break
                else:
                    in_range = False
        else:
            for value in range_1:
                if value in range_2:
                    in_range = True
                    break
                else:
                    in_range = False
        if in_range:
            overlap += 1
    print("Overlapping sections part 2: {}".format(overlap))

day4_part1("day4.txt")
day4_part2("day4.txt")