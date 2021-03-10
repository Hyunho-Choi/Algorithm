import sys
import collections

def s_input():
    return sys.stdin.readline().strip()

def DP():
    N = int(s_input())
    lis = list(map(int, s_input().split()))

    buffer = [1] * len(lis)

    for i in range(len(lis)):
        for j in range(i):
            if (lis[j] < lis[i]):
                buffer[i] = max(buffer[i], buffer[j]+1)

    print(max(buffer))

def Bina():
    N = int(s_input())
    lis = list(map(int, s_input().split()))

    buffer = [-1]

    for i in range(len(lis)):
        if buffer[len(buffer)-1] < lis[i]:
            buffer.append(lis[i])
        else:
            buffer[lowerBound(buffer, lis[i])] = lis[i]

    print(len(buffer)-1)

def lowerBound(li, find):
    start = 0
    end = len(li)-1

    while(start < end):
        mid = (end + start) // 2

        if find > li[mid]:
            start = mid+1
        elif find <= li[mid]:
            end = mid

    return start

if __name__ == '__main__':
    Bina()
