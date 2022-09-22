if __name__ == '__main__':
    N = int(input())
    stamps = []
    for i in range(N):
        a = input().upper()
        stamps.append(a)
    stamps = set(stamps)
    print(len(stamps))
