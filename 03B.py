# Backpacks


def openFile():
    return open("03Input", "r")


def forLine(file):
    lines = file.readlines()
    points = 0
    linesStorage = []
    for line in lines:
        linesStorage.append(line.rstrip())
        if len(linesStorage) == 3:
            characters = ''.join(set(linesStorage[0]).intersection(linesStorage[1]))
            character = ''.join(set(characters).intersection(linesStorage[2]))

            if character.isupper():
                points += ord(character) - 38
            else:
                points += ord(character) - 96
            linesStorage.clear()

    return points


print(forLine(openFile()))
