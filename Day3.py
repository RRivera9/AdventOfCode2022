import string

with open("Day3Input.txt") as f:
    puzzle = f.read().split("\n")

values = {}
for count, i in enumerate(string.ascii_lowercase + string.ascii_uppercase):
    values[i] = count + 1


def part1():
    score = 0
    for i in puzzle:
        midpoint = int(len(i) / 2)
        firsthalf = i[:midpoint]
        secondhalf = i[midpoint:]
        common = list(set(firsthalf) & set(secondhalf))
        score += values[common[0]]
    return score


def part2():
    score = 0

    # line below just divides all the rucksacks into groups of 3, then gives me a tuple of the 3 rucksacks
    for i in zip(*(iter(puzzle),) * 3):
        first, second, third = set(i[0]), set(i[1]), set(i[2])
        common = list(first & second & third)
        score += values[common[0]]
    return score


if __name__ == "__main__":
    print("Part 1 Answer:")
    print(part1())
    print("Part 2 Answer:")
    print(part2())
