import re

def solution(new_id):
    answer = re.sub('[^a-z0-9-_.]','', new_id.lower())
    for _ in range(7):
        answer = answer.replace('..','.')
    answer = answer.strip('.')
    if(len(answer) == 0):
        answer = 'a'
    if(len(answer) > 15):
        answer = answer[0:15]
    answer = answer.rstrip('.')
    while len(answer) < 3:
        answer += answer[len(answer)-1]
    return answer
