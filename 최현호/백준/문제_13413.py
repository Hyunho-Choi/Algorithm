import operator
from sys import stdin

cutNum, totalNum = list(map(int, stdin.readline().split()))
dic = {}
for i in range(totalNum):
    curNum = stdin.readline().split()[0]
    dic[curNum] = i

lisResult = sorted(dic.items(), key = operator.itemgetter(1))

if len(lisResult) < cutNum:
    for i in range(len(lisResult)):
        print(lisResult[i][0])
else:
    for i in range(cutNum):
        print(lisResult[i][0])

