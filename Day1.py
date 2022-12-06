with open("Day1Input.txt") as f:
    puzzle = f.read().split("\n")

def part1():
    bestcount = 0
    currentcount = 0
    for i in puzzle:
        if i == "":
            if currentcount > bestcount:
                bestcount = currentcount
            currentcount = 0
        else:
            currentcount += int(i)
    return bestcount

def part2():
    topthree = []
    currentcount = 0
    for i in puzzle:
        if i == "":
            if len(topthree) < 3:
                topthree.append(int(currentcount))
                topthree.sort()
            elif currentcount > topthree[0]:
                topthree.pop(0)
                topthree.append(currentcount)
                topthree.sort()
            currentcount = 0
        else:
            currentcount += int(i)
    return sum(topthree)



if __name__ == "__main__":
    print("Part 1 Answer:")
    print(part1())
    print("Part 2 Answer:")
    print(part2())