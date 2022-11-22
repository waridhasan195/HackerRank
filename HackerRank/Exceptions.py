# https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true




T = int(input())
result = []
for i in range(T):
        try:
                a,b=map(int,input().split())
                result.append(a//b)
        except Exception as e:
                result.append(e)
for i in result:
        if type (i) == int:
                print(i)
        else:
                print("Error Code:",i)
