# Signals


def openFile():
    return open("06Input", "r")


def forLine(file):
    lines = file.readlines()
    charactersLoadedCount = 0
    array = []
    arrayLoaded = False

    for line in lines:
        for character in line:

            # Loading array
            if not arrayLoaded:
                arrayLoaded = True if charactersLoadedCount == 13 else False

            else:
                # Check if unique
                if len(set(array)) == len(array):
                    return charactersLoadedCount
                # Load new values
                array.pop(0)

            array.append(character)
            charactersLoadedCount += 1


print(forLine(openFile()))
