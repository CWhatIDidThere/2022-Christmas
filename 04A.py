# Duplicite Duty


def openFile():
    return open("04Input", "r")


def forLine(file):
    lines = file.readlines()
    points = 0
    for line in lines:
        twoElves = line.split(",")
        firstElf = twoElves[0].split("-")
        secondElf = twoElves[1].split("-")

        if int(firstElf[0]) >= int(secondElf[0]) and int(firstElf[1]) <= int(secondElf[1]):
            points += 1
        elif int(secondElf[0]) >= int(firstElf[0]) and int(secondElf[1]) <= int(firstElf[1]):
            points += 1

    return points


print(forLine(openFile()))
