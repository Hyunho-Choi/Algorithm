import sys

def s_input():
    return sys.stdin.readline().strip()

def inputSize():
    NM = list(map(int, s_input().split()))
    return NM

def inputGetter(size):
    field = []
    for _ in range(size[0]):
        field.append(list(map(int, s_input().split())))
    return field

def checkBar(board, size):
    max = 0
    #세로 바
    for i in range(size[0] - 3):
        for j in range(size[1]):
            sum = board[i][j] + board[i+1][j] + board[i+2][j] + board[i+3][j]
            if sum > max:
                max = sum
    #가로 바
    for i in range(size[0]):
        for j in range(size[1] - 3):
            sum = board[i][j] + board[i][j+1] + board[i][j+2] + board[i][j+3]
            if sum > max:
                max = sum

    #사각형
    for i in range(size[0] - 1):
        for j in range(size[1] - 1):
            sum = board[i][j] + board[i][j+1] + board[i+1][j] + board[i+1][j+1]
            if sum > max:
                max = sum

    #L자 세로1
    for i in range(size[0] - 2):
        for j in range(size[1] - 1):
            sum = board[i][j] + board[i+1][j] + board[i+2][j] + board[i+2][j+1]
            if sum > max:
                max = sum

    #L자 세로2
    for i in range(size[0] - 2):
        for j in range(size[1] - 1):
            sum = board[i][j] + board[i][j+1] + board[i+1][j+1] + board[i+2][j+1]
            if sum > max:
                max = sum

    #L자 반전 세로1
    for i in range(size[0] - 2):
        for j in range(size[1] - 1):
            sum = board[i][j+1] + board[i+1][j+1] + board[i+2][j+1] + board[i+2][j]
            if sum > max:
                max = sum

    #L자 반전 세로2
    for i in range(size[0] - 2):
        for j in range(size[1] - 1):
            sum = board[i][j] + board[i][j+1] + board[i+1][j] + board[i+2][j]
            if sum > max:
                max = sum

    #L자 가로 좌상
    for i in range(size[0] - 1):
        for j in range(size[1] - 2):
            sum = board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j]
            if sum > max:
                max = sum

    #L자 가로 우상
    for i in range(size[0] - 1):
        for j in range(size[1] - 2):
            sum = board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j+2]
            if sum > max:
                max = sum

    #L자 가로 좌하
    for i in range(size[0] - 1):
        for j in range(size[1] - 2):
            sum = board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+1][j+2]
            if sum > max:
                max = sum

    #L자 가로 우하
    for i in range(size[0] - 1):
        for j in range(size[1] - 2):
            sum = board[i+1][j] + board[i+1][j+1] + board[i+1][j+2] + board[i][j+2]
            if sum > max:
                max = sum

    #번개 세로
    for i in range(size[0] - 2):
        for j in range(size[1] - 1):
            sum = board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+2][j+1]
            if sum > max:
                max = sum

    #번개 반전 세로
    for i in range(size[0] - 2):
        for j in range(size[1] - 1):
            sum = board[i][j+1] + board[i+1][j+1] + board[i+1][j] + board[i+2][j]
            if sum > max:
                max = sum

    #번개 가로
    for i in range(size[0] - 1):
        for j in range(size[1] - 2):
            sum = board[i][j] + board[i][j+1] + board[i+1][j+1] + board[i+1][j+2]
            if sum > max:
                max = sum

    #번개 반전 가로
    for i in range(size[0] - 1):
        for j in range(size[1] - 2):
            sum = board[i+1][j] + board[i+1][j+1] + board[i][j+1] + board[i][j+2]
            if sum > max:
                max = sum

    #법규 세로 좌측
    for i in range(size[0] - 2):
        for j in range(size[1] - 1):
            sum = board[i][j+1] + board[i+1][j+1] + board[i+2][j+1] + board[i+1][j]
            if sum > max:
                max = sum

    #법규 세로 우측
    for i in range(size[0] - 2):
        for j in range(size[1] - 1):
            sum = board[i][j] + board[i+1][j] + board[i+2][j] + board[i+1][j+1]
            if sum > max:
                max = sum

    #법규 가로 상
    for i in range(size[0] - 1):
        for j in range(size[1] - 2):
            sum = board[i+1][j] + board[i+1][j+1] + board[i+1][j+2] + board[i][j+1]
            if sum > max:
                max = sum

    #법규 가로 하
    for i in range(size[0] - 1):
        for j in range(size[1] - 2):
            sum = board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j+1]
            if sum > max:
                max = sum


    return max


if __name__ == '__main__':
    size = inputSize()
    board = inputGetter(size)
    print(checkBar(board, size))
