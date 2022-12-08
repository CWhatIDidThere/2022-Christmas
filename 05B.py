# Crane operator


def openFile():
    return open("05Input", "r")


def forLine(file):
    lines = file.readlines()
    ret = ''
    linesTemp = []
    cratePositionsLoaded = False
    cratePositions = [[], [], [], [], [], [], [], [], []]
    for line in lines:
        if line.strip() and not cratePositionsLoaded:
            linesTemp.append(line)
        elif not cratePositionsLoaded:
            cratePositionsLoaded = True
            # Loading the arrays of crate positions
            for stack in range(0, 9):
                pos = 1 + stack * 4
                for i in range(len(linesTemp) - 2, -1, -1):
                    if linesTemp[i][pos] != ' ':
                        cratePositions[stack].append(linesTemp[i][pos])

        elif cratePositionsLoaded:
            # Moving the crates
            orders = line.rstrip().split(" ")
            for i in range(0, int(orders[1])):
                cratePositions[int(orders[5])-1].append(cratePositions[int(orders[3])-1][-1])
                cratePositions[int(orders[3])-1].pop()

    # Final
    for stack in range(0, 9):
        ret += cratePositions[stack][-1]

    return ret


print(forLine(openFile()))
