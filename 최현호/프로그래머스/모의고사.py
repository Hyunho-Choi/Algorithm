def solution(answers):
    rtn = []
    cnts = []
    maxs = []
    dart = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    for i in range(3):
        cnt = 0
        for j in range(len(answers)):
            if answers[j] == dart[i][j % len(dart[i])]:
                cnt += 1

        cnts.append(cnt)

    realmax = max(cnts)
    for i in range(3):
        if cnts[i] == realmax:
            maxs.append(i+1)

    return maxs
