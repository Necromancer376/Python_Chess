board = [[' ａ', ' ｂ', ' ｃ', ' ｄ', ' ｅ', ' ｆ', ' ｇ', ' ｈ', ' '],
         ['|', '♜', '|', '♞', '|', '♝', '|', '♛', '|', '♚', '|', '♝', '|', '♞', '|', '♜', '|'],
         ['|', '♟', '|', '♟', '|', '♟', '|', '♟', '|', '♟', '|', '♟', '|', '♟', '|', '♟', '|'],
         ['|', '_', '|', '_', '|', '_', '|', '_', '|', '_', '|', '_', '|', '_', '|', '_', '|'],
         ['|', '_', '|', '_', '|', '_', '|', '_', '|', '_', '|', '_', '|', '_', '|', '_', '|'],
         ['|', '_', '|', '_', '|', '_', '|', '_', '|', '_', '|', '_', '|', '_', '|', '_', '|'],
         ['|', '_', '|', '_', '|', '_', '|', '_', '|', '_', '|', '_', '|', '_', '|', '_', '|'],
         ['|', '♙', '|', '♙', '|', '♙', '|', '♙', '|', '♙', '|', '♙', '|', '♙', '|', '♙', '|'],
         ['|', '♖', '|', '♘', '|', '♗', '|', '♕', '|', '♔', '|', '♗', '|', '♘', '|', '♖', '|']]

column = "abcdefgh"
whitepieces = "♔♕♖♗♘♙"
blackpieces = "♚♛♜♝♞♟"
deadpieces = ""
x1 = 0
x2 = 0
y1 = ''
y2 = ''
temp1 = []
temp2 = []
isLegal = False
isCheckW = False
isCheckB = False
isMate = False
xc = 0
yc = 0
whitevalue = 39
blackvalue = 39
killcount = 0


def PrintBoard():
    global board
    for i in board:
        for j in i:
            print(j, end='')
        print()


def InputSystem():
    global x1, x2, y1, y2, isMate
    move = input("Move: ")
    if move == "Check Mate":
        isMate = True
    elif len(move) != 4:
        print("Invalid input")
    else:
        y1 = move[0]
        x1 = int(move[1])
        y2 = move[2]
        x2 = int(move[3])

    LegalMoves()


def LegalMoves():
    global x1, x2, y1, y2, board, column, isLegal, isCheckW, isCheckB
    piece = board[9 - x1][(2 * column.index(y1)) + 1]
    piece2 = board[9 - x2][(2 * column.index(y2)) + 1]
    isLegal = False

    if piece == '♙':
        if x1 == 2:
            if column.index(y1) == column.index(y2) and (x2 == (x1 + 2) or x2 == (x1 + 1)):
                isLegal = True
            else:
                isLegal = False
        elif not x1 == 2:
            if column.index(y1) == column.index(y2) and x2 == (x1 + 1):
                isLegal = True
            elif column.index(y1) == column.index(y2) and x2 == (x1 - 1):
                isLegal = True
            else:
                isLegal = False
        else:
            isLegal = False

    elif piece == '♟':
        if x1 == 7:
            if column.index(y1) == column.index(y2) and (x2 == (x1 - 2) or x2 == (x1 - 1)):
                isLegal = True
            else:
                isLegal = False
        elif not x1 == 7:
            if column.index(y1) == column.index(y2) and x2 == (x1 - 1):
                isLegal = True
            elif column.index(y1) == column.index(y2) and x2 == (x1 + 1):
                isLegal = True
            else:
                isLegal = False
        else:
            isLegal = False


    elif piece == '♘' or piece == '♞':
        if (column.index(y2) == (column.index(y1)+1) or column.index(y2) == (column.index(y1)-1)) and (x2 == (x1+2) or x2 == (x1-2)):
            isLegal = True
        elif (column.index(y2) == (column.index(y1)+2) or column.index(y2) == (column.index(y1)-2)) and (x2 == (x1+1) or x2 == (x1-1)):
            isLegal = True
        else:
            isLegal = False

    elif piece == '♖' or piece == '♜':
        if x1 == x2 or y1 == y2:
            isLegal = True
        else:
            isLegal = False

    elif piece == '♔' or piece == '♚':
        if column.index(y1) == column.index(y2) and x2 == (x1 + 1):
            isLegal = True
        elif column.index(y1) == column.index(y2) and x2 == (x1 - 1):
            isLegal = True
        else:
            isLegal = False

    elif piece == '♗' or piece == '♝':
        if abs(column.index(y2) - column.index(y1)) == abs(x2 - x1):
            isLegal = True
        else:
            isLegal = False

    elif piece == '♕' or piece == '♛':
        if abs(column.index(y2) - column.index(y1)) == abs(x2 - x1):
            isLegal = True
        elif x1 == x2 or y1 == y2:
            isLegal = True
        else:
            isLegal = False

    if piece in whitepieces and piece2 in whitepieces:
        isLegal = False
    elif piece in blackpieces and piece2 in blackpieces:
        isLegal = False

    if isCheckW:
        ChangeBoard()
        if isCheckW:
            isLegal = False

    return isLegal


def ChangeBoard():
    global x1, x2, y1, y2, temp1, temp2, board, whitepieces, blackpieces, isLegal, isCheckW, isCheckB, deadpieces, whitevalue, blackvalue

    Wpiecevalue = {'♕': 9, '♖': 5, '♗': 3, '♘': 3, '♙': 1}
    Bpiecevalue = {'♛': 9, '♜': 5, '♝': 3, '♞': 3, '♟': 1}

    if isLegal:
        temp1 = board[9 - x1][(2 * column.index(y1)) + 1]
        temp2 = board[9 - x2][(2 * column.index(y2)) + 1]

        if temp2 in whitepieces or temp2 in blackpieces:
            deadpieces += temp2
            temp2 = '_'
            if temp2 in whitepieces:
                whitevalue -= Wpiecevalue[temp2]
            elif temp2 in blackpieces:
                blackvalue -= Bpiecevalue[temp2]

        board[9 - x1][(2 * column.index(y1)) + 1] = temp2
        board[9 - x2][(2 * column.index(y2)) + 1] = temp1
    else:
        print("invalid move")


def CheckSystem():
    global board, x1, x2, y1, y2, column, isLegal, xc, yc, whitepieces, blackpieces, isCheckW, isCheckB

    nonlinear = '♝♞♟♗♘♙'
    nondiagonal = '♜♞♖♘'

# White King
    for i in range(1, len(board)):
        for j in range(1, 16):
            if board[i][j] == '♔':
                xc = i
                yc = j

    if board[xc][yc] == '♔':
        isCheckW = False

        # vertical front
        if not xc == 1:
            for i in range(xc-1, 0, -1):
                if (board[i][yc] in nonlinear or board[i][yc] in whitepieces) and not isCheckW:
                    isCheckW = False
                    break
                elif not board[i][yc] in nonlinear and not board[i][yc] in whitepieces and board[i][yc] in blackpieces:
                    isCheckW = True
                    break
        # vertical behind
        if not xc == 8:
            for i in range(len(board), xc):
                if (board[i][yc] in nonlinear or board[i][yc] in whitepieces) and not isCheckW:
                    isCheckW = False
                    break
                elif not board[i][yc] in nonlinear and not board[i][yc] in whitepieces and board[i][yc] in blackpieces:
                    isCheckW = True
                    break
        # horizontal left
        if not yc == 1:
            for i in range(1, yc, 2):
                if (board[xc][i] in nonlinear or board[xc][i] in whitepieces) and not isCheckW:
                    isCheckW = False
                    break
                elif not board[xc][i] in nonlinear and not board[xc][i] in whitepieces and board[xc][i] in blackpieces:
                    isCheckW = True
                    break
        # horizontal right
        if not yc == 15:
            for i in range(yc+2, len(board[xc]), 2):
                if (board[xc][i] in nonlinear or board[xc][i] in whitepieces) and not isCheckW:
                    isCheckW = False
                    break
                elif not board[xc][i] in nonlinear and not board[xc][i] in whitepieces and board[xc][i] in blackpieces:
                    isCheckW = True
                    break

        # front right
        i = xc - 1
        if not xc == 1 and not yc == 15:
            for j in range(yc+2, len(board[xc]), 2):
                if i > 0:
                    if (board[i][j] in nondiagonal or board[i][j] in whitepieces) and not isCheckW:
                        isCheckW = False
                        break
                    elif board[i][j] not in nondiagonal and board[i][j] in blackpieces and not board[i][j] in whitepieces:
                        isCheckW = True
                        break
                    i -= 1
                else:
                    break
        # front left
        i = xc - 1
        if not xc == 1 and not yc == 1:
            for j in range(1, yc, -2):
                if i > 0:
                    if (board[i][j] in nondiagonal or board[i][j] in whitepieces) and not isCheckW:
                        isCheckW = False
                        break
                    elif board[i][j] not in nondiagonal and board[i][j] in blackpieces and not board[i][j] in whitepieces:
                        isCheckW = True
                        break
                    i -= 1
                else:
                    break
        # behind right
        i = xc + 1
        if not xc == 8 and not yc == 15:
            for j in range(yc+2, len(board[xc]), 2):
                if i < len(board):
                    if (board[i][j] in nondiagonal or board[i][j] in whitepieces) and not isCheckW:
                        isCheckW = False
                        break
                    elif board[i][j] not in nondiagonal and board[i][j] in blackpieces and not board[i][j] in whitepieces:
                        isCheckW = True
                        break
                    i += 1
                else:
                    break
        # behind left
        i = xc + 1
        if not xc == 8 and not yc == 1:
            for j in range(1, yc, -2):
                if i < len(board):
                    if (board[i][j] in nondiagonal or board[i][j] in whitepieces) and not isCheckW:
                        isCheckW = False
                        break
                    elif board[i][j] not in nondiagonal and board[i][j] in blackpieces and not board[i][j] in whitepieces:
                        isCheckW = True
                        break
                    i += 1
                else:
                    break

        # Kight checks
        if not xc >= 7 and not yc >= 15:
            if board[xc+2][yc+2] == '♞':
                isCheckW = True
        if not xc >= 8 and not yc >= 13:
            if board[xc+1][yc+4] == '♞':
                isCheckW = True
        if not xc >= 7 and not yc <= 1:
            if board[xc+2][yc-2] == '♞':
                isCheckW = True
        if not xc >= 8 and not yc <= 3:
            if board[xc+1][yc-4] == '♞':
                isCheckW = True
        if not xc <= 2 and not yc >= 15:
            if board[xc-2][yc+2] == '♞':
                isCheckW = True
        if not xc <= 1 and not yc >= 13:
            if board[xc-1][yc+4] == '♞':
                isCheckW = True
        if not xc <= 2 and not yc <= 1:
            if board[xc-2][yc-2] == '♞':
                isCheckW = True
        if not xc <= 1 and not yc <= 3:
            if board[xc-1][yc-4] == '♞':
                isCheckW = True


# Black King
    for i in range(1, len(board)):
        for j in range(1, 16):
            if board[i][j] == '♚':
                xc = i
                yc = j

    if board[xc][yc] == '♚':
        isCheckB = False

        # vertical front
        if not xc == 1:
            for i in range(xc-1, 0, -1):
                if (board[i][yc] in nonlinear or board[i][yc] in blackpieces) and not isCheckB:
                    isCheckB = False
                    break
                elif not board[i][yc] in nonlinear and not board[i][yc] in blackpieces and board[i][yc] in whitepieces:
                    isCheckB = True
                    break
        # vertical behind
        if not xc == 8:
            for i in range(xc+1, len(board)):
                print(board[i][yc])
                if (board[i][yc] in nonlinear or board[i][yc] in blackpieces) and not isCheckB:
                    isCheckB = False
                    break
                elif not board[i][yc] in nonlinear and not board[i][yc] in blackpieces and board[i][yc] in whitepieces:
                    isCheckB = True
                    break
        # horizontal left
        if not yc == 1:
            for i in range(1, yc, 2):
                if (board[xc][i] in nonlinear or board[xc][i] in blackpieces) and not isCheckB:
                    isCheckB = False
                    break
                elif not board[xc][i] in nonlinear and not board[xc][i] in blackpieces and board[xc][i] in whitepieces:
                    isCheckB = True
                    break
        # horizontal right
        if not yc == 15:
            for i in range(yc+2, len(board[xc]), 2):
                if (board[xc][i] in nonlinear or board[xc][i] in blackpieces) and not isCheckB:
                    isCheckB = False
                    break
                elif not board[xc][i] in nonlinear and not board[xc][i] in blackpieces and board[xc][i] in whitepieces:
                    isCheckB = True
                    break

        # front right
        i = xc - 1
        if not xc == 1 and not yc == 15:
            for j in range(yc+2, len(board[xc]), 2):
                if i > 0:
                    if (board[i][j] in nondiagonal or board[i][j] in blackpieces) and not isCheckB:
                        isCheckB = False
                        break
                    elif board[i][j] not in nondiagonal and board[i][j] in whitepieces and not board[i][j] in blackpieces:
                        isCheckB = True
                        break
                    i -= 1
                else:
                    break
        # front left
        i = xc - 1
        if not xc == 1 and not yc == 1:
            for j in range(1, yc, -2):
                if i > 0:
                    if (board[i][j] in nondiagonal or board[i][j] in blackpieces) and not isCheckB:
                        isCheckW = False
                        break
                    elif board[i][j] not in nondiagonal and board[i][j] in whitepieces and not board[i][j] in blackpieces:
                        isCheckB = True
                        break
                    i -= 1
                else:
                    break
        # behind right
        i = xc + 1
        if not xc == 8 and not yc == 15:
            for j in range(yc+2, len(board[xc]), 2):
                if i < len(board):
                    if (board[i][j] in nondiagonal or board[i][j] in blackpieces) and not isCheckB:
                        isCheckB = False
                        break
                    elif board[i][j] not in nondiagonal and board[i][j] in whitepieces and not board[i][j] in blackpieces:
                        isCheckB = True
                        break
                    i += 1
                else:
                    break
        # behind left
        i = xc + 1
        if not xc == 8 and not yc == 1:
            for j in range(1, yc, -2):
                if i < len(board):
                    if (board[i][j] in nondiagonal or board[i][j] in blackpieces) and not isCheckB:
                        isCheckB = False
                        break
                    elif board[i][j] not in nondiagonal and board[i][j] in whitepieces and not board[i][j] in blackpieces:
                        isCheckB = True
                        break
                    i += 1
                else:
                    break

        # Kight checks
        if not xc >= 7 and not yc >= 15:
            if board[xc+2][yc+2] == '♘':
                isCheckB = True
        if not xc >= 8 and not yc >= 13:
            if board[xc+1][yc+4] == '♘':
                isCheckB = True
        if not xc >= 7 and not yc <= 1:
            if board[xc+2][yc-2] == '♘':
                isCheckB = True
        if not xc >= 8 and not yc <= 3:
            if board[xc+1][yc-4] == '♘':
                isCheckB = True
        if not xc <= 2 and not yc >= 15:
            if board[xc-2][yc+2] == '♘':
                isCheckB = True
        if not xc <= 1 and not yc >= 13:
            if board[xc-1][yc+4] == '♘':
                isCheckB = True
        if not xc <= 2 and not yc <= 1:
            if board[xc-2][yc-2] == '♘':
                isCheckB = True
        if not xc <= 1 and not yc <= 3:
            if board[xc-1][yc-4] == '♘':
                isCheckB = True


def MateSystem():
    xcMate = 0
    ycMate = 0
    kingpositions = [False, False, False, False, False, False, False, False]

    if isCheckW:
        for i in range(1, len(board)):
            for j in range(1, 16):
                if board[i][j] == '♔':
                    xcMate = i
                    ycMate = j

        xc = max(xcMate-1, 1)
        CheckSystem()
        if isCheckW:
            kingpositions[0] = True

        xc = max(xcMate - 1, 1)
        yc = min(ycMate + 1, 15)
        CheckSystem()
        if isCheckW:
            kingpositions[0] = True

        yc = min(ycMate + 1, 15)
        CheckSystem()
        if isCheckW:
            kingpositions[0] = True

        xc = max(xcMate + 1, 1)
        yc = min(ycMate + 1, 15)
        CheckSystem()
        if isCheckW:
            kingpositions[0] = True

        xc = max(xcMate + 1, 1)
        CheckSystem()
        if isCheckW:
            kingpositions[0] = True

        xc = max(xcMate + 1, 1)
        yc = min(ycMate - 1, 15)
        CheckSystem()
        if isCheckW:
            kingpositions[0] = True

        yc = min(ycMate - 1, 15)
        CheckSystem()
        if isCheckW:
            kingpositions[0] = True

        xc = max(xcMate - 1, 1)
        yc = min(ycMate - 1, 15)
        CheckSystem()
        if isCheckW:
            kingpositions[0] = True

    if kingpositions:
        isMate = True


# def BoardValue():
#     global whitevalue, blackvalue, whitepieces, blackpieces, deadpieces, killcount
#
#     Wpiecevalue = {'♕':9, '♖':5, '♗':3, '♘':3, '♙':1}
#     Bpiecevalue = {'♛': 9, '♜': 5, '♝': 3, '♞': 3, '♟': 1}
#
#     for i in deadpieces:
#         if i in whitepieces:
#             whitevalue -= Wpiecevalue[i]
#         elif i in blackpieces:
#             blackvalue -= Bpiecevalue[i]

PrintBoard()
while not isMate:
    InputSystem()
    ChangeBoard()
    CheckSystem()
    PrintBoard()
    print("isCheck White: ", isCheckW)
    print("isCheck Black: ", isCheckB)
    print(deadpieces)
    print(whitevalue,blackvalue)
