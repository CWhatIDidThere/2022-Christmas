
#Backpacks


def openFile():
    return open("03Input", "r")


def forLine(file):
    lines = file.readlines()
    points = 0

    for line in lines:
        character = ''.join(set(line[0: int(len(line)/2)]).intersection(line[int(len(line)/2): len(line) - 1]))
        if character.isupper():
            points += ord(character) - 38
        else:
            points += ord(character) - 96
    return points


print(forLine(openFile()))



