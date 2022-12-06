with open("Day4Input.txt") as f:
    puzzle = f.read().split("\n")


def part1():
    score = 0
    for i in puzzle:
        left, right = i.split(",")
        leftstart, leftend = left.split("-")
        rightstart, rightend = right.split("-")
        leftrange, rightrange = range(int(leftstart), int(leftend)+1), range(int(rightstart), int(rightend)+1)
        leftset, rightset = set(leftrange), set(rightrange)
        intersection = (leftset & rightset)
        if (intersection == leftset) or (intersection == rightset):
            score += 1
    return score

def part2():
    score = 0
    for i in puzzle:
        left, right = i.split(",")
        leftstart, leftend = left.split("-")
        rightstart, rightend = right.split("-")
        leftrange, rightrange = range(int(leftstart), int(leftend) + 1), range(int(rightstart), int(rightend) + 1)
        leftset, rightset = set(leftrange), set(rightrange)
        intersection = (leftset & rightset)
        if len(intersection) > 0:
            score += 1
    return score


if __name__ == "__main__":
    print("Part 1 Answer:")
    print(part1())
    print("Part 2 Answer:")
    print(part2())