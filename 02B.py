
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
        'X': 0,
        'Y': 3,
        'Z': 6
    }[x]


def checkIfWon(opponent, me):
    ret = 0
    if opponent == 'A':
        if me == 'X':
            ret += 3
        elif me == 'Y':
            ret += 1
        elif me == 'Z':
            ret += 2
    elif opponent == 'B':
        if me == 'X':
            ret += 1
        elif me == 'Y':
            ret += 2
        elif me == 'Z':
            ret += 3
    elif opponent == 'C':
        if me == 'X':
            ret += 2
        elif me == 'Y':
            ret += 3
        elif me == 'Z':
            ret += 1

    ret += f(me)
    return ret


print(forLine(openFile()))



