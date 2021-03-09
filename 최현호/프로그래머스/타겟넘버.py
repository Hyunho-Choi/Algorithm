
def calculator(num1, num2, calcul):
    if calcul == 0:
        return num1 + num2
    elif calcul == 1:
        return num1 - num2

global list
global cnt

def solution(numbers, target):
    global list
    global cnt
    cnt = 0
    list = numbers

    dfs(0, 0, target)

    return cnt

def dfs(sum, index, target):
    global list
    global cnt
    if(index >= len(list)):
        if sum == target:
            cnt += 1
        return

    dfs(calculator(sum, list[index], 0), index + 1 ,target)
    dfs(calculator(sum, list[index], 1), index + 1 ,target)
    return


