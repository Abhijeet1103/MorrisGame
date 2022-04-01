iFile = 'board1.txt'

with open(iFile, 'r') as f:
    input = f.read()
    char = list(input)


def generateAdd(input):
    l = []
    wString = "W"

    for i in range(len(input)):
        if input[i] == "x":
            cboard = list(input)
            cboard[i] = wString

    print(cboard)

      #  l.__add__(cboard)


generateAdd(input)
