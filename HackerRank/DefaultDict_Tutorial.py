
# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true




# from collections import defaultdict

# n, m = list(map(int, input().split()))

# d = defaultdict(list)
# for i in range(n):
#     d['A'].append(input())

# for i in range(m):
#     d['B'].append(input())




# https://www.hackerrank.com/challenges/defaultdict-tutorial/forum

from collections import defaultdict

n, m = map(int, input().split())

A = []
for i in range(1, n+1):
    A.append(input())

B = []
for i in range(m):
    B.append(input())

d = defaultdict(list)

for i in B:
    if i not in d: # do not append again
        if i not in A:
            d[i].append(-1)

        else:
            for j in range(0,n):
                if A[j] == i:
                    d[i].append(j+1)

    print(*d[i])
    