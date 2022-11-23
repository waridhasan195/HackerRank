
# https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true


for _ in range(int(input())):
    _= input()
    A = set(map(int,input().split()))
    _=input()
    B = set(map(int,input().split()))
    print(len(B.difference(A)) == len(B)-len(A))