# Trees visible

def openFile():
    return open("08Input", "r")


def forLine(file):
    lines = file.readlines()
    count = 0
    forrestWidth = len(lines[0].rstrip())
    forrestHeight = len(lines)

    for hIdx, line in enumerate(lines):
        if hIdx == 0 or hIdx == forrestHeight - 1:
            continue
        for wIdx, tree in enumerate(line.rstrip()):
            isHidden = False
            if wIdx == 0 or wIdx == forrestWidth - 1:
                continue
            # TOP
            for i in range(hIdx - 1, -1, -1):
                if tree > lines[i][wIdx]:
                    continue
                else:
                    isHidden = True
                    break

            if not isHidden:
                count += 1
                continue
            isHidden = False
            # BOT
            for i in range(hIdx + 1, forrestHeight):
                if tree > lines[i][wIdx]:
                    continue
                else:
                    isHidden = True
                    break
            if not isHidden:
                count += 1
                continue
            isHidden = False
            # LEFT
            for i in range(wIdx - 1, -1, -1):
                if tree > lines[hIdx][i]:
                    continue
                else:
                    isHidden = True
                    break
            if not isHidden:
                count += 1
                continue
            isHidden = False
            # RIGHT
            for i in range(wIdx + 1, forrestWidth):
                if tree > lines[hIdx][i]:
                    continue
                else:
                    isHidden = True
                    break
            if not isHidden:
                count += 1
                continue

    count += (forrestWidth * 2) + (forrestHeight * 2) - 4

    return count


print(forLine(openFile()))
