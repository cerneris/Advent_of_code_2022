def day6(file, diff_count_size):
    with open(file, "r") as f:
        data = f.read()
    check_str = ""
    diff_count = 0
    for char_num in range(len(data)):
        for char in data[char_num::]:
            if char in check_str:
                diff_count = 0
                check_str = ""
                break
            else:
                check_str += char
                diff_count += 1
            if diff_count == diff_count_size:
                return char_num + len(check_str)

result_day1 = day6("day6.txt", 4)
result_day2 = day6("day6.txt", 14)

print("Result for a difference of 4 characters: {}".format(result_day1))
print("Result for a difference of 14 characters: {}".format(result_day2))