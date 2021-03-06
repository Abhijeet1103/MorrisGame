'''
The parameter for running this file are: board3.txt board4.txt depth
the first parameter is the input file
the second parameter is the output file generated by the program
the third parameter is the depth(integer)
'''
import sys


def closeMill(i: int, b: list):
    c = b[i]
    if c == 'W' or c == 'B':
        if i == 0:
            if (b[2] == c and b[4] == c) or (b[6] == c and b[18] == c):
                return True
            else:
                return False
        if i == 1:
            if (b[3] == c and b[5] == c) or (b[11] == c and b[20] == c):
                return True
            else:
                return False
        if i == 2:
            if (b[0] == c and b[4] == c) or (b[7] == c and b[15] == c):
                return True
            else:
                return False
        if i == 3:
            if (b[1] == c and b[5] == c) or (b[10] == c and b[17] == c):
                return True
            else:
                return False
        if i == 4:
            if (b[2] == c and b[0] == c) or (b[8] == c and b[12] == c):
                return True
            else:
                return False
        if i == 5:
            if (b[1] == c and b[3] == c) or (b[9] == c and b[14] == c):
                return True
            else:
                return False
        if i == 6:
            if (b[7] == c and b[8] == c) or (b[18] == c and b[0] == c):
                return True
            else:
                return False
        if i == 7:
            if (b[6] == c and b[8] == c) or (b[2] == c and b[15] == c):
                return True
            else:
                return False
        if i == 8:
            if (b[6] == c and b[7] == c) or (b[4] == c and b[12] == c):
                return True
            else:
                return False
        if i == 9:
            if (b[10] == c and b[11] == c) or (b[5] == c and b[14] == c):
                return True
            else:
                return False
        if i == 10:
            if (b[9] == c and b[11] == c) or (b[3] == c and b[17] == c):
                return True
            else:
                return False
        if i == 11:
            if (b[9] == c and b[10] == c) or (b[1] == c and b[20] == c):
                return True
            else:
                return False
        if i == 12:
            if (b[13] == c and b[14] == c) or (b[4] == c and b[8] == c):
                return True
            else:
                return False
        if i == 13:
            if (b[12] == c and b[14] == c) or (b[16] == c and b[19] == c):
                return True
            else:
                return False
        if i == 14:
            if (b[12] == c and b[13] == c) or (b[17] == c and b[20] == c):
                return True
            else:
                return False
        if i == 15:
            if (b[16] == c and b[17] == c) or (b[12] == c and b[18] == c):
                return True
            else:
                return False
        if i == 16:
            if (b[15] == c and b[17] == c) or (b[13] == c and b[19] == c):
                return True
            else:
                return False
        if i == 17:
            if (b[15] == c and b[16] == c) or (b[14] == c and b[20] == c):
                return True
            else:
                return False
        if i == 18:
            if (b[19] == c and b[20] == c) or (b[12] == c and b[15] == c):
                return True
            else:
                return False
        if i == 19:
            if (b[18] == c and b[20] == c) or (b[16] == c and b[13] == c):
                return True
            else:
                return False
        if i == 20:
            if (b[14] == c and b[17] == c) or (b[11] == c and b[1] == c):
                return True
            else:
                return False


def generateRemove(b, l):
    copyL = l.copy()
    for i in range(len(b)):
        if b[i] == 'B':
            if not closeMill(i, b):
                copyB =  list(b)
                copyB[i] = 'x'
                copyL.append(''.join(copyB))
            else:
                copyL.append(b)
    return copyL


def generateAdd(input: list):
    l = []
    b = []
    for i in range(len(input)):
        if input[i] == 'x':
            b = list(input)
            b[i] = "W"
            if closeMill(i, b):
                l = generateRemove(''.join(b), l)
            else:
                l.append(''.join(b))
    return l

def swapped(input):
    cBoard = list(input)
    for i in range(len(cBoard)):
        if cBoard[i] == 'W':
            cBoard[i] = 'B'
        elif cBoard[i] == 'B':
            cBoard[i] = 'W'

    return cBoard

def generateBlackMoves(input):
    bBoard = swapped(input)
    bMoves = generateMovesMidgameEndgame(''.join(bBoard))
    bList = swapped(bMoves)
    return bList


def StaticEstimation(input):
    black = 0
    white = 0
    bMoves = len(generateBlackMoves(input))
    for i in input:
        if i == "W":
            white += 1
        elif i == "B":
            black += 1

    if black <= 2:
        return 10000
    elif white <= 2:
        return -10000
    elif bMoves == 0:
        return 10000
    else:
        return (1000 * (white - black)) - bMoves


def generateHopping(input):
    l = []
    for i in range(len(input)):
        if input[i] == 'W':
            for j in range(len(input)):
                if input[j] == 'x':
                    cBoard = list(input)
                    cBoard[i] = 'x'
                    cBoard[j] = 'W'
                    if closeMill(j, cBoard):
                        l = generateRemove(''.join(cBoard), l)
                    else:
                        l.append(''.join(cBoard))
    return l


def neighbor(i):

    if i == 0:
        return [6,2,1]
    elif i == 1:
        return [0,3,11]
    elif i == 2:
        return [3,4,7, 0]
    elif i == 3:
        return [1, 2, 5, 10]
    elif i == 4:
        return [2, 5, 8]
    elif i == 5:
        return [4, 3, 19]
    elif i == 6:
        return [0, 7, 18]
    elif i == 7:
        return [6, 8, 2, 15]
    elif i == 8:
        return [4, 7, 12]
    elif i == 9:
        return [14, 5, 10]
    elif i == 10:
        return [3, 17, 11, 9]
    elif i == 11:
        return [1, 10, 20]
    elif i == 12:
        return [8, 13, 15]
    elif i == 13:
        return [12, 14, 16]
    elif i == 14:
        return [9, 13, 17]
    elif i == 15:
        return [12, 16, 18, 7]
    elif i == 16:
        return [13, 15, 17, 19]
    elif i == 17:
        return [10, 16, 20, 14]
    elif i == 18:
        return [6, 19, 15]
    elif i == 19:
        return [16, 18, 20]
    elif i == 20:
        return [11, 17, 19]



def generateMove(input):
    l = []
    for i in range(len(input)):
        if input[i] == 'W':
            x = neighbor(i)
            for n in x:
                if input[n] == 'x':
                    cBoard = list(input)
                    cBoard[i] = 'x'
                    cBoard[n] = 'W'
                    if closeMill(n, cBoard):
                        generateRemove(''.join(cBoard), l)
                    else:
                        l.append(''.join(cBoard))
    return l



def generateMovesMidgameEndgame(input):

    white = 0
    black = 0
    for i in input:
        if i == 'W':
            white += 1
        elif i == 'B':
            black += 1
    if white == 3:
        return generateHopping(input)
    else:
        return generateMove(input)



def MaxMin(input, depth, alpha, beta):
    global estimate
    global position_evaluated
    maxC: str
    if depth == 0:
        position_evaluated += 1

    elif depth > 0:
        depth -= 1
        x = -999999
        l = generateAdd(input)
        for i in l:
            minBoard = MinMax(i, depth, alpha, beta)
            if x < StaticEstimation(minBoard):
                x = StaticEstimation(minBoard)
                if estimate != 10000 or estimate != -10000:
                    estimate = x
                maxC = i
            if x >= beta:
                return maxC
            else:
                alpha = max(alpha, x)
        return maxC
    return input


def MinMax(input, depth, alpha, beta):
    global position_evaluated
    global estimate
    minC: str

    if depth == 0:
        position_evaluated += 1
    elif depth > 0:
        depth -= 1
        posX = 999999
        l = generateAdd(input)
        for i in l:
            maxBoard = MaxMin(i, depth, alpha, beta)
            if posX > StaticEstimation(maxBoard):
                posX = StaticEstimation(maxBoard)
                minC = i
            if posX <= alpha:
                return minC
            else:
                beta = min(beta,posX)
        return minC
    return input

def main():
    global position_evaluated
    global estimate
    alpha = -999999
    beta = 999999

    position_evaluated = 0
    estimate = 0
    iFile = sys.argv[1]
    oFile = sys.argv[2]
    depth = int(sys.argv[3])


    with open(iFile, 'r') as f:
        input = f.read()
        char = list(input)

    result = MaxMin(char, depth, alpha, beta)
    print("Board Position:",result)
    print("Positions Evaluated", position_evaluated)
    print("static estimation:", estimate)
    with open(oFile, 'w') as f:
        f.write(result)



if __name__ == '__main__':
    main()
