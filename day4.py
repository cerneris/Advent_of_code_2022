def day4_part1(file):
    with open(file, "r") as f:
        data = f.readlines()
    overlap = 0
    for line in data:
        section_1, section_2 = line.split(",")
        section_1_start, section_1_stop = map(int, section_1.split("-"))
        section_2_start, section_2_stop = map(int, section_2.split("-"))
        range_1 = set(range(section_1_start, section_1_stop + 1))
        range_2 = set(range(section_2_start, section_2_stop + 1))
        if range_2.issubset(range_1) or range_1.issubset(range_2):
            overlap += 1
            continue
    print("Overlapping sections part 1: {}".format(overlap))

def day4_part2(file):
    with open(file, "r") as f:
        data = f.readlines()
    overlap = 0
    for line in data:
        section_1, section_2 = line.split(",")
        section_1_start, section_1_stop = map(int, section_1.split("-"))
        section_2_start, section_2_stop = map(int, section_2.split("-"))
        range_1 = range(section_1_start, section_1_stop + 1)
        range_2 = range(section_2_start, section_2_stop + 1)
        in_range = False
        for value in range_1:
            if value in range_2:
                overlap += 1
                break
                
    print("Overlapping sections part 2: {}".format(overlap))

day4_part1("day4.txt")
day4_part2("day4.txt")