
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

# n, m = map(int, input().split())

# A = []
# for i in range(n):
#     A.append(input())
# print("A: ", A)

# B = []
# for i in range(m):
#     B.append(input())
# print("B: ", B)


# d = defaultdict(list)

# print("Default List: ", d)


# for i in B:
#     if i not in d:
#         if i not in A:
#             d.append[-1]
#         else:
#             for j in range(n):
#                 if A[j] == i:
#                     d[i].append(j+1)
#     print(*d[i])
# print(d)



n = int(input())
d = dict(list())

for i in range(1, n+1):
    v = input()


    if v in d:
        d[v].append(i)
    else:
        d[v]=[i]
# d.[v].append(i) if we use defaultdict


for key, val in d.items():
    print(key, val)











# for i in B:
#     if i not in d: # do not append again
#         if i not in A:
#             d[i].append(-1)

#         else:
#             for j in range(0,n):
#                 if A[j] == i:
#                     d[i].append(j+1)

#     print(*d[i])



