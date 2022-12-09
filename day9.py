import math

def calculate_distance(x1, x2, y1, y2):
    distance = math.sqrt(((x2 - x1) ** 2) + (y2 - y1) ** 2)
    return distance

def ret_movement(move):
    match move:
        case "U":
            movement = (0, 1)
        case "D":
            movement = (0, -1)
        case "R":
            movement = (1, 0)
        case "L":
            movement = (-1, 0)
    return movement

def tuple_difference(head, tail):
    head_x, head_y = head
    tail_x, tail_y = tail
    diff = (head_x - tail_x, head_y - tail_y)
    diff = ((min(1, max(-1, diff[0]))), (min(1, max(-1, diff[1]))))
    return calculate_new_location(tail, diff)

def calculate_new_location(point, movement):
    return tuple(map(sum, zip(point, movement)))   

def move_to(head, tail):
    distance = calculate_distance(head[0], tail[0], head[1], tail[1])
    if distance >= 1.5:
        tail = tuple_difference(head, tail)
    return tail

def day9_part1(file):
    with open(file, "r") as f:
        data = f.read().splitlines()
    # X, Y
    head = (0, 0)
    tail = (0, 0)
    tail_visits = set()
    temp_head = None
    for line in data:
        move, amount = line.split(" ")
        amount = int(amount)
        for i in range(amount):
            head = calculate_new_location(head, ret_movement(move))
            tail = move_to(head, tail)
            tail_visits.add(tail)
    print("Total amount of tail visits: {}".format(len(tail_visits)))

def day9_part2(file):
    with open(file, "r") as f:
        data = f.read().splitlines()
    # X, Y
    tails = [(0,0) for x in range(10)]
    tail_visits = set()
    for line in data:
        move, amount = line.split(" ")
        amount = int(amount)
        for i in range(amount):
            tails[0] = calculate_new_location(tails[0], ret_movement(move))
            for tail in range(0, len(tails) - 1):
                tails[tail + 1] = move_to(tails[tail], tails[tail + 1])            
            tail_visits.add(tails[9])
    print("Total amount of tail visits: {}".format(len(tail_visits)))

day9_part1("day9.txt")
day9_part2("day9.txt")