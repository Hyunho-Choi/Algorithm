import copy

def rotated(a):
    n = len(a)
    m = len(a[0])

    result = [[0]* n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

def solution(key, lock):
    offset = len(key)-1
    base_board = [[-2] * (len(lock) + offset*2) for _ in range((len(lock) + offset*2))]
   
    for i in range(len(key)):
        for j in range(len(key)):
            base_board[i+offset][j+offset] = lock[i][j]
    
    rot_keys = []
    for dir in range(4):
        rot_key = key[:]
        for _ in range(dir):
            rot_key = rotated(rot_key)
        rot_keys.append(rot_key)


    for i in range(len(lock) + len(key)-1):
        for j in range(len(lock) + len(key)-1):
            for dir in range(4):
                match = 0
                board = copy.deepcopy(base_board)

                for x in range(len(key)):
                    for y in range(len(key)):
                        board[i+x][j+y] += rot_keys[dir][x][y]

                for x in range(len(lock)):
                    for y in range(len(lock)):
                        if board[len(key)-1+x][len(key)-1+y] == 1:
                            match += 1
                
                board.clear()
                if match == len(lock)*len(lock):
                    return True

    return False
