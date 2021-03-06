import heapq
from sys import stdin

value = 0
stoneNum,bagNum = map(int, stdin.readline().strip().split())
stones = []
bags = []
ableStones = []
for i in range(stoneNum):
    temp = list(map(int, stdin.readline().strip().split()))
    heapq.heappush(stones, temp)
for f in range(bagNum):
    bags.append(int(stdin.readline().strip()))
bags.sort()
for j in bags:
    while stones and stones[0][0] <= j:
        heapq.heappush(ableStones, -heapq.heappop(stones)[1])
    if len(ableStones) > 0 :
        value -= heapq.heappop(ableStones)
    elif not stones:
        break
print(value)
