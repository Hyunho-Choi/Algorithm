result = 0
setup = input().split()
num_vilage = int(setup[0])
truck_max = int(setup[1])
num_data = int(input())
data = [None] * num_data
for i1 in range(num_data):
    data[i1] = input().split()
    data[i1][0] = int(data[i1][0])
    data[i1][1] = int(data[i1][1])
    data[i1][2] = int(data[i1][2])
space = [None] * (num_vilage-1)
for i2 in range(num_vilage-1):
    space[i2] = truck_max
solted_data = sorted(data, key = lambda x : (x[1], x[0]))
for i in solted_data:
    lenth = i[1] - i[0]
    sliced = space[i[0]-1:i[0]-1+lenth]
    this_min = min(sliced)
    if(this_min <= 0):
        continue
    if(this_min > i[2]):
        value = i[2]
        for j in range(lenth):
            space[i[0]-1 + j] -= value
        result += value
    elif(this_min > 0):
        result += this_min
        for j in range(lenth):
            space[i[0]-1 + j] -= this_min

print(result)
