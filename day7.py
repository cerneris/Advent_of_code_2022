from pathlib import Path
from collections import defaultdict

def day7_part1(file):
    # Create a path to start from root
    current_dir = Path("/")
    # Use defaultdict (Does not result in KeyErrors, if the key does not exist, returns integer with value 0 instead)
    dir_sizes = defaultdict(int)
    with open(file, "r") as f:
        for line in f.read().splitlines():
            # Use match statement to check the line split contents.
            match line.split():
                # If the command is cd, resolve to the correct directory.
                case ["$", "cd", newdir]:
                    current_dir = current_dir / newdir
                    current_dir = current_dir.resolve()
                # If the line contains the size, add size to current directories in current full path.
                # Ignore directories, because we do not need to verify they exist.
                case [file_size, file_name] if file_size.isdigit():
                    file_size = int(file_size)
                    for path in [current_dir, *current_dir.parents]:
                        # Add the file size to current directory and all parents.
                        dir_sizes[path] += file_size

        result = sum((dir_size for dir_size in dir_sizes.values() if dir_size <= 100000))
        print("Sum of all directories that are below 100000 in size: {}".format(result))

def day7_part2(file):
    # Create a path to start from root
    current_dir = Path("/")
    # Use defaultdict (Does not result in KeyErrors, if the key does not exist, returns integer with value 0 instead)
    dir_sizes = defaultdict(int)
    with open(file, "r") as f:
        for line in f.read().splitlines():
            # Use match statement to check the line split contents.
            match line.split():
                # If the command is cd, resolve to the correct directory.
                case ["$", "cd", newdir]:
                    current_dir = current_dir / newdir
                    current_dir = current_dir.resolve()
                # If the line contains the size, add size to current directories in current full path.
                # Ignore directories, because we do not need to verify they exist.
                case [file_size, file_name] if file_size.isdigit():
                    file_size = int(file_size)
                    for path in [current_dir, *current_dir.parents]:
                        # Add the file size to current directory and all parents.
                        dir_sizes[path] += file_size
        root = Path("/").resolve()
        # Get the total used space by getting the size of the root directory.
        total_used = dir_sizes[root]
        # Get the total space free
        total = 70000000 - total_used
        possible_dirsizes = []
        for dir_size in dir_sizes.values():
            # Get all directories that could be deleted to free enough space.
            if total + dir_size >= 30000000:
                possible_dirsizes.append(dir_size)
        print("Smallest directory size to remove: {}".format(min(possible_dirsizes)))

day7_part1("day7.txt")
day7_part2("day7.txt")