import operator

def solution(genres, plays):
    answer = []
    dic = {}
    dicCnt = {}

    for i in range(len(genres)):
        if(genres[i] in dic):
            dic.get(genres[i]).append([i,plays[i]])
            dicCnt[genres[i]] = dicCnt.get(genres[i]) + plays[i]
        else:
            dic[genres[i]] = [[i, plays[i]]]
            dicCnt[genres[i]] = plays[i]

    dicCntList = sorted(dicCnt.items(), key=operator.itemgetter(1), reverse = True)

    for iter in dicCntList:
        putResult = sorted(dic[iter[0]], key=operator.itemgetter(1), reverse = True)
        for song in range(len(putResult)):
            if(song >= 2):
                break;
            if(putResult[song] == None):
                continue
            answer.append(putResult[song][0])

    return answer
