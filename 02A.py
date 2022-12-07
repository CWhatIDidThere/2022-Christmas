
#How many total Calories is that Elf carrying?


def openFile():
    return open("01AInput", "r")


def forLine(file):
    lines = file.readlines()
    maximum = -1
    localMax = 0
    for line in lines:
        if line.strip():
            localMax += int(line)
        else:
            if localMax > maximum:
                maximum = localMax
            localMax = 0

    if localMax > maximum:
        maximum = localMax
    return maximum


print(forLine(openFile()))
