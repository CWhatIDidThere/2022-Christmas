# Parser


def openFile():
    return open("07Input", "r")


# SCHEME OF DICK
# DirName: [Bool, Size, ['dir'], ['filename']]
# DirName[0]: Bool if the size is fully counted
# DirName[1]: Calculated size (if [0] is true then this is final size)
# DirName[2]: Array of stings of names of the directories contained
# DirName[3]: Array of stings of names of the files contained


def forLine(file):
    lines = file.readlines()
    dick = {}
    currentDict = []

    for line in lines:
        # Lexical + Syntax
        splitLine = line.split(" ")
        if splitLine[0] == '$':
            if splitLine[1] == 'cd':
                if splitLine[2] == '/':
                    # Only once - Skip
                    currentDict.append('/')
                elif splitLine[2] == '..':
                    currentDict.pop()
                else:
                    currentDict.append(splitLine[2])
            else:
                skipIsRealIDontNeedThisLSCheckAsITrustThemSoNoSyntaxCheck = True

        elif splitLine[0] == 'dir':
            if splitLine[1] in dick:
                # Add new dir under this dir
                if splitLine[1] not in dick[currentDict[-1]][2]:
                    dick[splitLine[1]] = dick[currentDict[-1]][2].append(splitLine[1])
            # Create new
            else:
                dick[splitLine[1]] = [False, 0, [splitLine[1]], []]
        # FILE
        else:
            if splitLine[1] in dick:
                # Add new file under this dir
                if splitLine[1] not in dick[currentDict[-1]][3]:
                    # TODO Check if legit!!!
                    dick[splitLine[1]] = dick[currentDict[-1]][3].append(splitLine[1])
                    dick[splitLine[1]] = dick[currentDict[-1]][1] + int(splitLine[0])
            # Create new
            else:
                dick[splitLine[1]] = [False, int(splitLine[0]), [], [splitLine[1]]]

    return dick


print(forLine(openFile()))
