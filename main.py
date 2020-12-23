board = [[' ａ', ' ｂ', ' ｃ', ' ｄ', ' ｅ', ' ｆ', ' ｇ', ' ｈ', ],
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
    global board, isLegal
    for i in board:
        for j in i:
            print(j, end='')
        print()


def InputSystem():
    global x1, x2, y1, y2
    y1 = input('column1:')
    x1 = int(input('row1:'))
    y2 = input('column2:')
    x2 = int(input('row2:'))
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


def CheckSystem():
    global board, x1, x2, y1, y2, column, isLegal, xc, yc, whitepieces, blackpieces, isCheckW, isCheckB

    for i in range(len(board)):
        for j in range(i):
            if board[i][j] == '♔':
                xc = i
                yc = j
    if board[xc][yc] == '♔':
        for i in range(xc, 1, -1):
            if not board[7 - i][(2 * i)-1] == '＿' or board[7 - i][(2 * i)-1] in whitepieces:
                isCheckW = False
                break

            elif board[7 - i][(2 * i)-1] == '♞' or board[7 - i][(2 * i)-1] == '♜':
                isCheckW = False
                break

            elif i == (xc - 1) and board[7 - i][(2 * i)-1] == '♟':
                isCheckW = True
                break

            elif board[7 - i][(2 * i)-1] == '♛' or board[7 - i][(2 * i)-1] == '♝':
                isCheckW = True
                break

        for i in range(xc, 8):
            if not board[11 - i][(2 * i)+1] == '＿' or board[11 - i][(2 * i)+1] in whitepieces:
                isCheckW = False
                break

            elif board[11 - i][(2 * i)+1] == '♞' or board[11 - i][(2 * i)+1] == '♜':
                isCheckW = False
                break

            elif i == (xc + 1) and board[11 - i][(2 * i)+1] == '♟':
                isCheckW = True
                break

            elif board[11 - i][(2 * i)+1] == '♛' or board[11 - i][(2 * i)+1] == '♝':
                isCheckW = True
                break

        for i in range(xc, 0, -1):
            if board[9 - i][(2 * yc)-1] == '＿' or board[9 - i][(2 * yc)-1] in whitepieces:
                isCheckW = False
                break

            elif board[9 - i][(2 * yc)-1] == '♛' or board[9 - i][(2 * yc)-1] == '♜':
                isCheckW = True
                break

        for i in range(xc, 8):
            if board[9 - i][(2 * yc)+1] == '＿' or board[9 - i][(2 * yc)+1] in whitepieces:
                isCheckW = False
                break

            elif board[9 - i][(2 * yc)+1] == '♛' or board[9 - i][(2 * yc)+1] == '♜':
                isCheckW = True
                break

        if board[(9 - xc)+2][((2 * yc)-1)+1] == '♞' or board[(9 - xc)-2][((2 * yc)-1)-1] == '♞':
            isCheckW = True

        elif board[(9 - xc)+2][((2 * yc)-1)-1] == '♞' or board[(9 - xc)-2][((2 * yc)-1)+1] == '♞':
            isCheckW = True
        elif board[(9 - xc)+1][((2 * yc)-1)+2] == '♞' or board[(9 - xc)-1][((2 * yc)-1)-2] == '♞':
            isCheckW = True
        elif board[(9 - xc)-1][((2 * yc)-1)+2] == '♞' or board[(9 - xc)+1][((2 * yc)-1)-2] == '♞':
            isCheckW = True
        else:
            isCheckW = False

    for i in range(len(board)):
        for j in range(i):
            if board[i][j] == '♚':
                xc = i
                yc = j
    if board[xc][yc] == '♚':
        isCheckB = False

    return isCheckW, isCheckB


PrintBoard()
for m in range(10):
    InputSystem()
    ChangeBoard()
    PrintBoard()
