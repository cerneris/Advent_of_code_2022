def day10_part1(file):
    with open(file, "r") as f:
        data = f.read().splitlines()
    cur_cycle = 0
    x = 1
    total = 0
    for line in data:
        match line.split():
            case ['addx', num]:
                for i in range(2):
                    cur_cycle += 1
                    if cur_cycle in (20, 60, 100, 140, 180, 220):
                        total += cur_cycle * x
                x += int(num)
            case ['noop']:
                cur_cycle += 1
                if cur_cycle in (20, 60, 100, 140, 180, 220):
                    total += cur_cycle * x
    print("Total signal strength: {}".format(total))

def day10_part2(file):
    with open(file, "r") as f:
        data = f.read().splitlines()
    cur_cycle = 0
    x = 1
    total = 0
    print("CRT IMAGE: \n")
    for line in data:
        match line.split():
            case ['addx', num]:
                for i in range(2):
                    if cur_cycle % 40 in (x - 1, x, x + 1):
                        print("#", end="")
                    else:
                        print(".", end="")
                    cur_cycle += 1
                    if cur_cycle % 40 == 0:
                        print()
                x += int(num)
            case ['noop']:
                if cur_cycle % 40 in (x - 1, x, x + 1):
                    print("#", end="")
                else:
                    print(".", end="")
                cur_cycle += 1
                if cur_cycle % 40 == 0:
                        print()

day10_part1("day10.txt")
day10_part2("day10.txt")