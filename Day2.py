with open("Day2Input.txt") as f:
    puzzle = f.read().split("\n")

def part1():
    # rock is a, x
    # paper is b, y
    # scissors is c, z
    score = 0
    points = {"a x": 4, "b x": 1, "c x": 7, "a y": 8, "b y": 5, "c y": 2, "a z": 3, "b z": 9, "c z": 6}
    for i in puzzle:
        code = i.lower()
        score += points[code]
    return score

def part2():
    points = {"a x": 3, "b x": 1, "c x": 2, "a y": 4, "b y": 5, "c y": 6, "a z": 8, "b z": 9, "c z": 7}
    score = 0
    for i in puzzle:
        code = i.lower()
        score += points[code]
    return score



if __name__ == "__main__":
    print("Part 1 Answer:")
    print(part1())
    print("Part 2 Answer:")
    print(part2())