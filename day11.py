import re
from collections import deque
import math

def day11_part1(file):
    with open(file, "r") as f:
        data = f.read().split("\n\n")
    monkey_data = dict()
    for monkey in data:
        monkey_info = monkey.split("\n")
        for info in monkey_info:
            info = info.strip()
            match info.split(" "):
                case ["Monkey", num]:
                    monkey_data[num.strip(":")] = {}
                    cur_monkey = num.strip(":")
                case ["Starting", "items:", *num]:
                    monkey_data[cur_monkey]["items"] = deque(map(int, re.findall("\\d+", str(num))))
                case["Operation:", "new", "=", *operation]:
                    monkey_data[cur_monkey]["oper"] = operation
                case["Test:", *test]:
                    monkey_data[cur_monkey]['divisor'] = int(re.findall("\\d+", str(test))[0])
                case["If", "true:", *true]:
                    monkey_data[cur_monkey]['truestate'] = re.findall("\\d+", str(true))[0]
                case["If", "false:", *false]:
                    monkey_data[cur_monkey]['falsestate'] = re.findall("\\d+", str(false))[0]
    inspections = [0 for x in range(len(monkey_data))]
    for i in range(20):
        for data in monkey_data:
            operation = " ".join(monkey_data[data]['oper'])
            while monkey_data[data]['items']:
                inspections[int(data)] += 1
                item = monkey_data[data]['items'][0]
                print("Current item: {}".format(item))
                match operation.split(" "):
                    case ["old", "*", "old"]:
                        print("New item: {}".format(math.floor(item * item / 3)))
                        monkey_data[data]['items'][0] = math.floor(item * item / 3)
                    case ["old", "+", "old"]:
                        print("New item: {}".format(math.floor((item + item) / 3)))
                        monkey_data[data]['items'][0] = math.floor((item + item) / 3)
                    case ["old", "*", num]:
                        print("New item: {}".format(math.floor((item * int(num)) / 3)))
                        monkey_data[data]['items'][0] = math.floor(item * int(num) / 3)
                    case ["old", "+", num]:
                        print("New item: {}".format(math.floor((item + int(num)) / 3)))
                        monkey_data[data]['items'][0] = math.floor((item + int(num)) / 3)
                item = monkey_data[data]['items'][0]
                print("{} divided by {}.".format(item, monkey_data[data]['divisor']))
                if item % monkey_data[data]['divisor'] == 0:
                    new_monkey = monkey_data[data]['truestate']
                    print("Throw to monkey: {}".format(new_monkey))
                    monkey_data[new_monkey]['items'].append(monkey_data[data]['items'].popleft())
                    print(monkey_data[new_monkey]['items'])
                else:
                    new_monkey = monkey_data[data]['falsestate']
                    print("Throw to monkey: {}".format(new_monkey))
                    monkey_data[new_monkey]['items'].append(monkey_data[data]['items'].popleft())
                    print(monkey_data[new_monkey]['items'])
    first = max(inspections)
    inspections.remove(first)
    second = max(inspections)

    print("Level of monkey business: {}".format(first*second))
    
def day11_part2(file):
    pass

day11_part1("day11.txt")