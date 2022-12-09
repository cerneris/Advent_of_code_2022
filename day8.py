from math import prod

def day8_part1(file):
    with open(file, "r") as f:
        grid = f.read().splitlines()
    visible_trees = 0
    # Go through all the trees.
    for ti, row in enumerate(grid):
        for tj, tree in enumerate(row):
            # Check every possible angle, if tree is higher than one of them it is visible from somewhere.
            if all(grid[ti][j] < tree for j in range(0, tj)):
                visible_trees += 1
            elif all(grid[ti][j] < tree for j in range(tj + 1, len(row))):
                visible_trees += 1
            elif all(grid[i][tj] < tree for i in range(0, ti)):
                visible_trees += 1
            elif all(grid[i][tj] < tree for i in range(ti + 1, len(grid))):
                visible_trees += 1
            else:
                continue
    print("Total amount of visible trees: {}".format(visible_trees))

def day8_part2(file):
    with open(file, "r") as f:
        grid = f.read().splitlines()
    scenic_scores = []

    for ti, row in enumerate(grid):
        for tj, tree in enumerate(row):
            # Add empty point list for tree.
            scenic_scores.append([0, 0, 0, 0])
            # Check every possible angle to see how many trees it can see, add a point for every tree found.
            # Every time a taller tree is found, it will block the rest of the trees. (BREAK)
            for j in range(tj - 1, -1, -1):
                scenic_scores[-1][0] += 1
                if grid[ti][j] >= tree:
                    break
            for i in range(ti - 1, -1, -1):
                scenic_scores[-1][1] += 1
                if grid[i][tj] >= tree:
                    break
            for j in range(tj + 1, len(row)):
                scenic_scores[-1][2] += 1
                if grid[ti][j] >= tree:
                    break
            for i in range(ti + 1, len(grid)):
                scenic_scores[-1][3] += 1
                if grid[i][tj] >= tree:
                    break
    # Get the max from all the products of each tree.
    print("Max scenic score for any tree on grid: {}".format(max(prod(scenic_score) for scenic_score in scenic_scores)))

day8_part1("day8.txt")
day8_part2("day8.txt")