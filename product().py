import itertools
from itertools import product

A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort()
c = list(product(A,B))
print(*c)
