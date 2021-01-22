import math
def solution(progresses, speeds):
    
    answer = []
    head = 0
    remains = [0] * len(progresses)
    for i in range(len(progresses)):
        remains[i] = int(math.ceil(float(100 - progresses[i]) / float(speeds[i])))
        
    cnt = 0
    top = remains[0]
    for i in range(len(remains)):
        if(i + 1 == len(remains)):
            cnt += 1
            answer.append(cnt)
            cnt = 0
        
        elif(top < remains[i+1]):
            cnt += 1
            answer.append(cnt)
            top = remains[i+1]
            cnt = 0
            
        else:
            cnt += 1
    
    return answer
