from itertools import product as p
A=map(int,input().split())
B=map(int,input().split())    
print(*p(A,B))