board = [[' ａ', ' ｂ', ' ｃ', ' ｄ', ' ｅ', ' ｆ', ' ｇ', ' ｈ', ' '],
         ['|', '♜', '|', '♞', '|', '♝', '|', '♛', '|', '♚', '|', '♝', '|', '♞', '|', '♜', '|'],
         ['|', '♟', '|', '♟', '|', '♟', '|', '♟', '|', '♟', '|', '♟', '|', '♟', '|', '♟', '|'],
         ['|', '＿', '|', '＿', '|', '＿', '|', '＿', '|', '＿', '|', '＿', '|', '＿', '|', '＿', '|'],
         ['|', '＿', '|', '＿', '|', '＿', '|', '＿', '|', '＿', '|', '＿', '|', '＿', '|', '＿', '|'],
         ['|', '＿', '|', '＿', '|', '＿', '|', '＿', '|', '＿', '|', '＿', '|', '＿', '|', '＿', '|'],
         ['|', '＿', '|', '＿', '|', '＿', '|', '＿', '|', '＿', '|', '＿', '|', '＿', '|', '＿', '|'],
         ['|', '♙', '|', '♙', '|', '♙', '|', '♙', '|', '♙', '|', '♙', '|', '♙', '|', '♙', '|'],
         ['|', '♖', '|', '♘', '|', '♗', '|', '♕', '|', '♔', '|', '♗', '|', '♘', '|', '♖', '|']]

column = "abcdefgh"
whitepieces = "♔♕♖♗♘♙"
blackpieces = '♚♛♜♝♞♟'

x1 = 0
x2 = 0
y1 = ''
y2 = ''
temp1 = []
temp2 = []
isLegal = False
isCheckW = False
isCheckB = False
xc = 0
yc = 0


def PrintBoard():
    global board
    for i in board:
        for j in i:
            print(j, end='')
        print()


def InputSystem():
    global x1, x2, y1, y2
    move = input("Move: ")
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
    global x1, x2, y1, y2, temp1, temp2, board, whitepieces, blackpieces, isLegal, isCheckW, isCheckB
    if isLegal:
        temp1 = board[9 - x1][(2 * column.index(y1)) + 1]
        temp2 = board[9 - x2][(2 * column.index(y2)) + 1]

        if temp2 in whitepieces or temp2 in blackpieces:
            temp2 = '＿'

        board[9 - x1][(2 * column.index(y1)) + 1] = temp2
        board[9 - x2][(2 * column.index(y2)) + 1] = temp1
    else:
        print("invalid move")


# def CheckSystem():
#     global board, x1, x2, y1, y2, column, isLegal, xc, yc, whitepieces, blackpieces, isCheckW, isCheckB
#
#     for i in range(1, len(board)):
#         for j in range(0, 17):
#             if board[i][j] == '♔':
#                 xc = i
#                 yc = int(j / 2)
#
#     print(xc, yc)
#     if board[xc][yc] == '♔':
#         for i in range(xc, 1, -1):
#             if not board[7 - i][(2 * i)-1] == '＿' or board[7 - i][(2 * i)-1] in whitepieces:
#                 isCheckW = False
#                 break
#
#             elif board[7 - i][(2 * i)-1] == '♞' or board[7 - i][(2 * i)-1] == '♜':
#                 isCheckW = False
#                 break
#
#             elif i == (xc - 1) and board[7 - i][(2 * i)-1] == '♟':
#                 isCheckW = True
#                 break
#
#             elif board[7 - i][(2 * i)-1] == '♛' or board[7 - i][(2 * i)-1] == '♝':
#                 isCheckW = True
#                 break
#
#         for i in range(xc, 8):
#             if not board[11 - i][(2 * i)+1] == '＿' or board[11 - i][(2 * i)+1] in whitepieces:
#                 isCheckW = False
#                 break
#
#             elif board[11 - i][(2 * i)+1] == '♞' or board[11 - i][(2 * i)+1] == '♜':
#                 isCheckW = False
#                 break
#
#             elif i == (xc + 1) and board[11 - i][(2 * i)+1] == '♟':
#                 isCheckW = True
#                 break
#
#             elif board[11 - i][(2 * i)+1] == '♛' or board[11 - i][(2 * i)+1] == '♝':
#                 isCheckW = True
#                 break
#
#         for i in range(xc, 0, -1):
#             if board[9 - i][(2 * yc)-1] == '＿' or board[9 - i][(2 * yc)-1] in whitepieces:
#                 isCheckW = False
#                 break
#
#             elif board[9 - i][(2 * yc)-1] == '♛' or board[9 - i][(2 * yc)-1] == '♜':
#                 isCheckW = True
#                 break
#
#         for i in range(xc, 8):
#             if board[9 - i][(2 * yc)+1] == '＿' or board[9 - i][(2 * yc)+1] in whitepieces:
#                 isCheckW = False
#                 break
#
#             elif board[9 - i][(2 * yc)+1] == '♛' or board[9 - i][(2 * yc)+1] == '♜':
#                 isCheckW = True
#                 break
#
#         if board[(9 - xc)+2][((2 * yc)-1)+1] == '♞' or board[(9 - xc)-2][((2 * yc)-1)-1] == '♞':
#             isCheckW = True
#
#         elif board[(9 - xc)+2][((2 * yc)-1)-1] == '♞' or board[(9 - xc)-2][((2 * yc)-1)+1] == '♞':
#             isCheckW = True
#         elif board[(9 - xc)+1][((2 * yc)-1)+2] == '♞' or board[(9 - xc)-1][((2 * yc)-1)-2] == '♞':
#             isCheckW = True
#         elif board[(9 - xc)-1][((2 * yc)-1)+2] == '♞' or board[(9 - xc)+1][((2 * yc)-1)-2] == '♞':
#             isCheckW = True
#         else:
#             isCheckW = False
#
#     for i in range(1, len(board)):
#         for j in range(0, 17):
#             if board[i][j] == '♚':
#                 xc = i
#                 yc = int(j / 2)
#
#     print(xc, yc)
#     if board[xc][yc] == '♚':
#         for i in range(xc, 1, -1):
#             if not board[7 - i][(2 * i)-1] == '＿' or board[7 - i][(2 * i)-1] in blackpieces:
#                 isCheckB = False
#                 break
#
#             elif board[7 - i][(2 * i)-1] == '♘' or board[7 - i][(2 * i)-1] == '♖':
#                 isCheckB = False
#                 break
#
#             elif i == (xc - 1) and board[7 - i][(2 * i)-1] == '♟':
#                 isCheckB = True
#                 break
#
#             elif board[7 - i][(2 * i)-1] == '♕' or board[7 - i][(2 * i)-1] == '♗':
#                 isCheckB = True
#                 break
#
#         for i in range(xc, 8):
#             if not board[11 - i][(2 * i)+1] == '＿' or board[11 - i][(2 * i)+1] in blackpieces:
#                 isCheckB = False
#                 break
#
#             elif board[11 - i][(2 * i)+1] == '♘' or board[11 - i][(2 * i)+1] == '♖':
#                 isCheckB = False
#                 break
#
#             elif i == (xc + 1) and board[11 - i][(2 * i)+1] == '♙':
#                 isCheckB = True
#                 break
#
#             elif board[11 - i][(2 * i)+1] == '♕' or board[11 - i][(2 * i)+1] == '♗':
#                 isCheckB = True
#                 break
#
#         for i in range(xc, 0, -1):
#             if board[9 - i][(2 * yc)-1] == '＿' or board[9 - i][(2 * yc)-1] in blackpieces:
#                 isCheckW = False
#                 break
#
#             elif board[9 - i][(2 * yc)-1] == '♕' or board[9 - i][(2 * yc)-1] == '♖':
#                 isCheckW = True
#                 break
#
#         if board[(9 - xc)+2][((2 * yc)-1)+1] == '♘' or board[(9 - xc)-2][((2 * yc)-1)-1] == '♘':
#             isCheckB = True
#
#         elif board[(9 - xc)+2][((2 * yc)-1)-1] == '♘' or board[(9 - xc)-2][((2 * yc)-1)+1] == '♘':
#             isCheckB = True
#         elif board[(9 - xc)+1][((2 * yc)-1)+2] == '♘' or board[(9 - xc)-1][((2 * yc)-1)-2] == '♘':
#             isCheckB = True
#         elif board[(9 - xc)-1][((2 * yc)-1)+2] == '♘' or board[(9 - xc)+1][((2 * yc)-1)-2] == '♘':
#             isCheckB = True
#         else:
#             isCheckB = Fals
def CheckSystem():
    global board, x1, x2, y1, y2, column, isLegal, xc, yc, whitepieces, blackpieces, isCheckW, isCheckB

    nonlinear = '♝♞♟♗♘♙'
    nondiagonal = '♜♞♖♘'

    # position of white king
    for i in range(1, len(board)):
        for j in range(1, 16):
            if board[i][j] == '♔':
                xc = i
                yc = j

    if board[xc][yc] == '♔':
        isCheckW = False

        # vertical front
        for i in range(xc-1, 0, -1):
            if (board[i][yc] in nonlinear or board[i][yc] in whitepieces) and not isCheckW:
                isCheckW = False
                break
            elif not board[i][yc] in nonlinear and not board[i][yc] in whitepieces and board[i][yc] in blackpieces:
                isCheckW = True
                break
        # vertical behind
        for i in range(len(board), xc):
            if (board[i][yc] in nonlinear or board[i][yc] in whitepieces) and not isCheckW:
                isCheckW = False
                break
            elif not board[i][yc] in nonlinear and not board[i][yc] in whitepieces and board[i][yc] in blackpieces:
                isCheckW = True
                break
        # horizontal left
        for i in range(1, yc, 2):
            if (board[xc][i] in nonlinear or board[xc][i] in whitepieces) and not isCheckW:
                isCheckW = False
                break
            elif not board[xc][i] in nonlinear and not board[xc][i] in whitepieces and board[xc][i] in blackpieces:
                isCheckW = True
                break
        # horizontal right
        for i in range(yc+2, len(board[xc]), 2):
            if (board[xc][i] in nonlinear or board[xc][i] in whitepieces) and not isCheckW:
                isCheckW = False
                break
            elif not board[xc][i] in nonlinear and not board[xc][i] in whitepieces and board[xc][i] in blackpieces:
                isCheckW = True
                break

        # front right
        i = xc - 1
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
        i = xc
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
        i = xc
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

    for i in range(1, len(board)):
        for j in range(1, 16):
            if board[i][j] == '♚':
                xc = i
                yc = j

    if board[xc][yc] == '♚':
        isCheckB = False

        # vertical front
        for i in range(xc-1, 0, -1):
            if (board[i][yc] in nonlinear or board[i][yc] in blackpieces) and not isCheckB:
                isCheckB = False
                break
            elif not board[i][yc] in nonlinear and not board[i][yc] in blackpieces and board[i][yc] in whitepieces:
                isCheckB = True
                break
        # vertical behind
        for i in range(len(board), xc):
            if (board[i][yc] in nonlinear or board[i][yc] in blackpieces) and not isCheckB:
                isCheckB = False
                break
            elif not board[i][yc] in nonlinear and not board[i][yc] in blackpieces and board[i][yc] in whitepieces:
                isCheckB = True
                break
        # horizontal left
        for i in range(1, yc, 2):
            if (board[xc][i] in nonlinear or board[xc][i] in blackpieces) and not isCheckB:
                isCheckB = False
                break
            elif not board[xc][i] in nonlinear and not board[xc][i] in blackpieces and board[xc][i] in whitepieces:
                isCheckB = True
                break
        # horizontal right
        for i in range(yc+2, len(board[xc]), 2):
            if (board[xc][i] in nonlinear or board[xc][i] in blackpieces) and not isCheckB:
                isCheckB = False
                break
            elif not board[xc][i] in nonlinear and not board[xc][i] in blackpieces and board[xc][i] in whitepieces:
                isCheckB = True
                break

        # front right
        i = xc - 1
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
        i = xc
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
        i = xc
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


PrintBoard()
for m in range(10):
    InputSystem()
    ChangeBoard()
    CheckSystem()
    PrintBoard()
    print("isCheck White: ", isCheckW)
    print("isCheck Black: ", isCheckB)
