import re
import bisect

def solution(inf, query):
    answer = []
    db = {}
    lan = ['cpp', 'java', 'python', '-']
    job = ['backend', 'frontend', '-']
    cer = ['junior', 'senior', '-']
    food = ['chicken', 'pizza', '-']

    for l in lan:
        db[l] = {}
        for j in job:
            db[l][j] = {}
            for c in cer:
                db[l][j][c] = {}
                for f in food:
                    db[l][j][c][f] = []

    for i in inf:
        data = i.split()
        db[data[0]][data[1]][data[2]][data[3]].append(int(data[4]))
        db['-'][data[1]][data[2]][data[3]].append(int(data[4]))
        db[data[0]]['-'][data[2]][data[3]].append(int(data[4]))
        db[data[0]][data[1]]['-'][data[3]].append(int(data[4]))
        db[data[0]][data[1]][data[2]]['-'].append(int(data[4]))
        db['-']['-'][data[2]][data[3]].append(int(data[4]))
        db['-'][data[1]]['-'][data[3]].append(int(data[4]))
        db['-'][data[1]][data[2]]['-'].append(int(data[4]))
        db[data[0]]['-']['-'][data[3]].append(int(data[4]))
        db[data[0]]['-'][data[2]]['-'].append(int(data[4]))
        db[data[0]][data[1]]['-']['-'].append(int(data[4]))
        db['-']['-']['-'][data[3]].append(int(data[4]))
        db['-']['-'][data[2]]['-'].append(int(data[4]))
        db['-'][data[1]]['-']['-'].append(int(data[4]))
        db[data[0]]['-']['-']['-'].append(int(data[4]))
        db['-']['-']['-']['-'].append(int(data[4]))
        
    for l in lan:
        for j in job:
            for c in cer:
                for f in food:
                    db[l][j][c][f].sort()
    
    for q in query:
        s = re.split(' and | ', q)
        #db[s[0]][s[1]][s[2]][s[3]].sort()
        answer.append(len(db[s[0]][s[1]][s[2]][s[3]]) - bisect.bisect_left(db[s[0]][s[1]][s[2]][s[3]], int(s[4])))

    return answer
