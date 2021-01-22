import operator
from sys import stdin

global datas
global max
max = 0

def particle(startIndex, endIndex):
    global max
    global datas

    partDatas = datas[startIndex : endIndex]
    if(len(partDatas) <= 1):
        if(partDatas[0] > max):
            max = min(partDatas) * len(partDatas)
        del partDatas
        time.sleep(1)
        return

    if ((min(partDatas) * len(partDatas)) > max):
        max = min(partDatas) * len(partDatas)

    firstMin = partDatas.index(min(partDatas)) + startIndex


    if(not(startIndex >= firstMin)):
        if(firstMin - startIndex == 1):
            if(datas[startIndex] > max):
                max = datas[startIndex]
        else:
            particle(startIndex, firstMin)
    if(not(firstMin+1 >= endIndex)):
        if(endIndex - (firstMin+1) == 1):
            if(datas[firstMin+1] > max):
                max = datas[firstMin+1]
        else:
            particle(firstMin+1, endIndex)

def ProcessLine():
    answer = []
    while(True):
        global max
        global datas
        datas = list(map(int, input().split()))
        if(len(datas) <= 1):
            break

        dataSize = datas[0]
        datas = datas[1:]

        particle(0,len(datas))

        answer.append(max)
    for i in answer:
        print(i)

if __name__ == '__main__':
    #순회시작
    ProcessLine()


