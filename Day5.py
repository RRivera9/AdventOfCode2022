with open("Day5Input.txt") as f:
    puzzle = f.read().split("\n")

# hard coding first 10 lines of input
def createBoxes():
    starting_field = ["GFVHPS", "GJFBVDZM", "GMLJN", "NGZVDWP", "VRCB", "VRSMPWLZ", "THP", "QRSNCHZV", "FLGPVQJ"]
    boxes = {}
    for count, i in enumerate(starting_field):
        boxes[count + 1] = []
        for letter in i:
            boxes[count + 1].append(letter)
    return boxes

print(createBoxes())

def part1():
    boxes = createBoxes()
    final = []
    # hardcoded the boxes above so we can skip 10 lines
    for i in puzzle[10:]:
        command = i.split(" ")
        amount, start, destination = command[1], command[3], command[5]
        for j in range(int(amount)):
            box = boxes[int(start)].pop()
            boxes[int(destination)].append(box)
    for i in range(1,10):
        final.append(boxes[i][-1])
    final = "".join([x for x in final])
    return final

def part2():
    boxes = createBoxes()
    final = []
    # hardcoded the boxes above so we can skip 10 lines
    for i in puzzle[10:]:
        command = i.split(" ")
        amount, start, destination = command[1], command[3], command[5]
        # negative slice notation below, to get the boxes in the normal order, starting from last "amount" boxes
        movingboxes = boxes[int(start)][-int(amount):]
        for j in range(int(amount)):
            boxes[int(start)].pop()
        boxes[int(destination)] = boxes[int(destination)] + movingboxes
    for i in range(1, 10):
        final.append(boxes[i][-1])
    final = "".join([x for x in final])
    return final


if __name__ == "__main__":
    print("Part 1 Answer:")
    print(part1())
    print("Part 2 Answer:")
    print(part2())