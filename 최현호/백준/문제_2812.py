import sys

def s_input():
    return sys.stdin.readline().strip()

def baek2812():
    N,K = map(int,s_input().split())
    li = list(map(int,list(s_input())))
    stack = []
    delCnt = 0
    answer = ""
    end = False

    for i in range(N):

        if end:
            stack.append(li[i])
            continue

        while(True):
            if len(stack) == 0:
                stack.append(li[i])
                break

            if stack[len(stack)-1] >= li[i]:
                stack.append(li[i])
                break

            stack.pop()
            delCnt+=1
            if delCnt >= K:
                stack.append(li[i])
                end = True
                break


    for s in stack[0: N-K]:
        answer += str(s)

    print(answer)


if __name__ == '__main__':
    baek2812()
