
#How many total Calories is that Elf carrying? TOP3



def openFile():
    return open("01AInput", "r")


def forLine(file):
    lines = file.readlines()
    maximum = [0, 0, 0]
    localMax = 0
    for line in lines:
        if line.strip():
            localMax += int(line)
        else:
            maximum = checkAndChangeTheWinners(localMax, maximum)
            localMax = 0

    maximum = checkAndChangeTheWinners(localMax, maximum)
    return maximum[0] + maximum[1] + maximum[2]


def checkAndChangeTheWinners(localMax, maximum):
    if localMax > maximum[0]:
        maximum[2] = maximum[1]
        maximum[1] = maximum[0]
        maximum[0] = localMax
    elif localMax > maximum[1]:
        maximum[2] = maximum[1]
        maximum[1] = localMax
    elif localMax > maximum[2]:
        maximum[2] = localMax
    return maximum


print(forLine(openFile()))
