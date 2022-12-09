# Parser
from enum import Enum
global lessThan100000Size

def openFile():
    return open("07Input", "r")


# SCHEME OF DICK
# Dictionary Including Commands, oK?
# Version 1.1
# DirName: [Bool, Size, ['dir': []], ['filename']]
# DirName[0]: Bool if the size is fully counted
# DirName[1]: Calculated size (if [0] is true then this is final size)
# DirName[2]: Array of dictionaries of the directories contained
# DirName[3]: Array of stings of names of the files contained

class D(Enum):
    Bool = 0
    Size = 1
    Dir = 2
    File = 3


def forLine(file):
    lines = file.readlines()
    dick = {}
    currentDict = []
    lsCalled = False

    for line in lines:
        # Lexical + Syntax
        line = line.rstrip()
        splitLine: [str] = line.split(" ")

        if splitLine[0] == '$':
            if splitLine[1] == 'cd':
                if splitLine[2] == '..':
                    currentDict.pop()
                else:
                    currentDict.append(splitLine[2])
                lsCalled = False
            else:
                lsCalled = True

        elif splitLine[0] == 'dir':
            # print('FOUND DIR ' + splitLine[1])
            if currentDict[-1] in dick:
                # Add new dir under this dir
                # This is a hack. Not sure why it works like this
                # print('------')
                # print(dick)
                # print(currentDict[-1])
                # print(dick[currentDict[-1]])
                # print(dick[currentDict[-1]][2])
                if len(dick[currentDict[-1]][2]) == 0:
                    dick[currentDict[-1]][2] = {}
                if splitLine[1] not in dick[currentDict[-1]][2]:
                    dick[currentDict[-1]][2][str(splitLine[1])] = [False, 0, {}, []]
            # Create new
            else:
                dick[currentDict[-1]] = [False, 0, {splitLine[1]: [False, 0, {}, []]}, []]
                # print('NEW DIR')
        # FILE
        else:
            # print('FOUND FILE ' + splitLine[1])
            if currentDict[-1] in dick:
                # Add new file under this dir
                if splitLine[1] not in dick[currentDict[-1]][3]:
                    # TODO Check if legit!!!
                    dick[currentDict[-1]][3].append(splitLine[1])
                    dick[currentDict[-1]][1] = dick[currentDict[-1]][1] + int(splitLine[0])
            # Create new
            else:
                dick[currentDict[-1]] = [False, int(splitLine[0]), {}, [splitLine[1]]]
                # print('NEW FILE + DIR')

    print('-------Rec-------')
    # Binary tree count
    recursionWillSaveUsRight(dick['/'])

    return lessThan100000Size

# TODO WE GET NEW FOLDER - NAME + MY MASTER FOLDER
# TODO WE CREATE OUR STRUCT FOR THIS FOLDER
# TODO IS THERE LS ALWAYS?


lessThan100000Size = 0


def recursionWillSaveUsRight(recDick):
    print(recDick)
    print(recDick[D.Dir])
    print(recDick.keys())
    for folder in recDick[D.Dir].keys():
        recDick[D.Size] += recursionWillSaveUsRight(recDick[D.Dir][folder])

    recDick[D.Bool] = True
    if recDick[D.Size] > 100000:
        lessThan100000Size += 1
    return recDick[D.Size]


print(forLine(openFile()))
