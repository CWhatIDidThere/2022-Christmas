
#Backpacks

def openFile():
    return open("03Input", "r")


def forLine(file):
    lines = file.readlines()
    points = 0

    for line in lines:
        points += ord(line[0: len(line)/2 - 1].intersection(line[len(line)/2: len(line) - 1]))-96
    return points


print(forLine(openFile()))



