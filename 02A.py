
#Rock paper scisors


def openFile():
    return open("02Input", "r")


def forLine(file):
    lines = file.readlines()
    points = 0

    for line in lines:
        points += checkIfWon(line[0], line[2])
    return points


def f(x):
    return {
        'X': 1,
        'Y': 2,
        'Z': 3
    }[x]


def checkIfWon(opponent, me):
    ret = 0
    if opponent == 'A':
        if me == 'Y':
            ret += 6
        elif me == 'X':
            ret += 3
    elif opponent == 'B':
        if me == 'Z':
            ret += 6
        elif me == 'Y':
            ret += 3
    elif opponent == 'C':
        if me == 'X':
            ret += 6
        elif me == 'Z':
            ret += 3

    ret += f(me)
    return ret


print(forLine(openFile()))



