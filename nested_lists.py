if __name__ == '__main__':
    name = []
    score = []
    lists =[]
    final=[]
    for _ in range(int(input())):
        lists.append(input())
        lists.append(float(input()))
    i=0
    while i<len(lists):
        name.append(lists[i])
        i=i+2
    i=1
    while i<len(lists):
        score.append(lists[i])
        i=i+2
    new_score = []
    for i in score:
        if i not in new_score:
            new_score.append(i)
    new_score.sort()
    v=new_score[1]
    i=1
    while i<len(lists):
        if lists[i]== v:
            final.append(lists[i-1])
        i=i+2
    final.sort()
    for z in final:
        print (z)
