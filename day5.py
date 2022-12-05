import re
from collections import deque

def day5_part1(file):
    # Split the data to crates and moves from empty line.
    with open(file, "r") as f:
        crates, moves = f.read().split("\n\n")
    stacks = []
    for line in crates.splitlines():
        # Take every fourth letter (aka crate) from every line (starting from index 1) if the line is not empty append it to stacks.
        for placement, index in enumerate(range(1, len(line), 4)):
            # Create a stack for every crate placement area.
            while placement >= len(stacks):
                stacks.append(deque())
            # If the crate slot is not empty, add to correct stack.
            if line[index] != " ":
                stacks[placement].append(line[index])
    
    # Split the lines in moves and map the amount of crates to move from stack to another.
    for move in moves.splitlines():
        amount, _from, _to = map(int, re.findall("\d+", move))
        for i in range(amount):
            # Use the deque appendleft and popleft to move the crates around.
            stacks[_to - 1].appendleft(stacks[_from - 1].popleft())
    # Get all top crates from stacks.
    end_result = "".join(crate[0] for crate in stacks)
    print("The first crate in each stack: {}".format(end_result))
        
def day5_part2(file):
    # Split the data to crates and moves from empty line.
    with open(file, "r") as f:
        crates, moves = f.read().split("\n\n")
    stacks = []
    for line in crates.splitlines():
        # Take every fourth letter (aka crate) from every line (starting from index 1) if the line is not empty append it to stacks.
        for placement, index in enumerate(range(1, len(line), 4)):
            # Create a stack for every crate placement area.
            while placement >= len(stacks):
                stacks.append(deque())
            # If the crate slot is not empty, add to correct stack.
            if line[index] != " ":
                stacks[placement].append(line[index])
    
    # Split the lines in moves and map the amount of crates to move from stack to another.
    for move in moves.splitlines():
        amount, _from, _to = map(int, re.findall("\d+", move))
        # Create a temporary stack for movements.
        temp_stack = deque()
        for i in range(amount):
            # Remove from given stack and add to temporary stack
            temp_stack.appendleft(stacks[_from - 1].popleft())
        # Move whole temporary stack to given stack.
        stacks[_to - 1].extendleft(temp_stack)
    # Get all top crates from stacks.
    end_result = "".join(crate[0] for crate in stacks)
    print("The first crate in each stack: {}".format(end_result))

day5_part1("day5.txt")
day5_part2("day5.txt")