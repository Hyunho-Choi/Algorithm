import math

def solution(brown, yellow):
    answer = [0] * 2
    rt = pow(brown + 4, 2) / 4 - 4 * (brown + yellow)
    answer[0] = (int((brown + 4) / 4 + (math.sqrt(rt)) / 2))
    answer[1] = ((brown + 4) / 2) - answer[0]
    answer.sort(reverse=True)
    return answer
