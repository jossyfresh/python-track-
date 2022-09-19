if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(arr)
    x = []
    for y in arr:
        if y not in x :
            x.append(y)
    z = len(x)
    x.sort()
    print (x[z-2]) 
   
