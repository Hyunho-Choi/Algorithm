import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

for _ in range(int(input())):
    # 기본정보 부분
    nunTeam = int(input())
    ranking = list(map(int,input()))
    tree = [[] for _ in range(nunTeam+1)]
    inDegree=[0 for _ in range(nunTeam+1)]
    q = deque()
    for i in range(0, nunTeam-1):
        for j in range(i+1, nunTeam):
            tree[ranking[i]].append(ranking[j])
            inDegree[ranking[j]] += 1

    # 바뀐 순위 정리 부분
    m = int(sys.stdin.readline())
    for _ in range(m):
        change_a,change_b=map(int,sys.stdin.readline().split())
        check=True
        for i in tree[change_a]:
            if i==change_b:#change_a가 더 높은 순위 의 팀일때
                tree[change_a].remove(change_b)
                tree[change_b].append(change_a)
                inDegree[change_b]-=1
                inDegree[change_a]+=1
                check=False
        if check:#change_b가 더 높은 순위 의 팀일때
            tree[change_b].remove(change_a)
            tree[change_a].append(change_b)
            inDegree[change_a] -= 1
            inDegree[change_b] += 1

    #진입차수 0인거 찾기
    for i in range(1,nunTeam+1):
        if inDegree[i]==0:
            q.append(i)

    #반복부
    result=0
    result_list=[]
    if not q:
        result=1
    while q:
        if len(q)>1:
            result=1
            break
        a=q.popleft()
        result_list.append(a)
        for i in tree[a]:
            inDegree[i]-=1
            if inDegree[i]==0:
                q.append(i)
            elif inDegree[i]<0:
                result=1
                break

    if result>0 or len(result_list)<nunTeam:
        print('IMPOSSIBLE')
    else:
        print(*result_list)
 
