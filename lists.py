if __name__ == '__main__':
    N = int(input())
    lists = []
    for line in range(N):
        line = input().split()
        for j in range(1,len(line)):
            line[j]=int(line[j])
            
        if line[0]=='insert':
            lists.insert(line[1],line[2])
        elif line[0]=='remove':
            lists.remove(line[1])
        elif line[0]=='append':
            lists.append(line[1])
        elif line[0]=='sort':
            lists.sort()
        elif line[0]=='pop':
            lists.pop()
        elif line[0]=='reverse':
            lists.reverse()
        elif line[0]=='print':
            print(lists)
