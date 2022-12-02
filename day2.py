def day2_part1(file):
    win_combinations = {
        "A" : "Y",
        "B" : "Z",
        "C" : "X"
    }
    draw_combinations = {
        "A" : "X",
        "B" : "Y",
        "C" : "Z"
    }
    loss_combinations = {
        "A" : "Z",
        "B" : "X",
        "C" : "Y"
    }
    points = {
        "X" : "1",
        "Y" : "2",
        "Z" : "3",
        "win" : "6",
        "draw" : "3",
        "loss" : "0"
    }
    game_points = 0
    with open(file, "r") as f:
        data = f.readlines()
    for row in data:
        data_split = row.split(" ")
        enemy = data_split[0].strip()
        you = data_split[1].strip()
        if win_combinations[enemy] == you:
            # print("{} vs {}, you win.".format(enemy, you))
            game_points += int(points["win"])
            game_points += int(points[you])
        elif draw_combinations[enemy] == you:
            # print("{} vs {}, draw.".format(enemy, you))
            game_points += int(points["draw"])
            game_points += int(points[you])
        else:
            # print("{} vs {}, you lose.".format(enemy, you))
            game_points += int(points["loss"])
            game_points += int(points[you])
    print("Day 2 part 1 points: {}".format(game_points))

def day2_part2(file):
    game_outcomes = {
        "X" : "loss",
        "Y" : "draw",
        "Z" : "win"
    }
    win_combinations = {
        "A" : "paper",
        "B" : "scissors",
        "C" : "rock"
    }
    draw_combinations = {
        "A" : "rock",
        "B" : "paper",
        "C" : "scissors"
    }
    loss_combinations = {
        "A" : "scissors",
        "B" : "rock",
        "C" : "paper"
    }
    points = {
        "rock" : "1",
        "paper" : "2",
        "scissors" : "3",
        "win" : "6",
        "draw" : "3",
        "loss" : "0"
    }
    game_points = 0
    with open(file, "r") as f:
        data = f.readlines()
    for row in data:
        data_split = row.split(" ")
        enemy = data_split[0].strip()
        outcome = game_outcomes[data_split[1].strip()]
        if outcome == "win":
            choice = win_combinations[enemy]
            game_points += int(points[choice])
            game_points += int(points["win"])
            # print("Enemy choice: {}. You need to win so you choose {}.".format(enemy, choice))
        elif outcome == "draw":
            choice = draw_combinations[enemy]
            game_points += int(points[choice])
            game_points += int(points["draw"])
            # print("Enemy choice: {}. You need to get a draw so you choose {}.".format(enemy, choice))
        else:
            choice = loss_combinations[enemy]
            game_points += int(points[choice])
            game_points += int(points["loss"])
            # print("Enemy choice: {}. You need to lose so you choose {}.".format(enemy, choice))
    print("Day 2 part 2 points: {}".format(game_points))

day2_part1("day2.txt")
day2_part2("day2.txt")