if __name__ == '__main__':
    M = int(input())
    m = set(map(int,input().split()))
    N = int(input())
    n = set(map(int,input().split()))
    c = list(list(m.difference(n)) + list(n.difference(m)))
    c.sort()
    for x in c:
        print(x)
