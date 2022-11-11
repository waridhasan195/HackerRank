
from itertools import combinations

n = int(input())
l = list(input().split())
k = int(input())

com = list(combinations(l, k))


count = 0
for i in com:
    if 'a' in i:
        count += 1
print(count/len(com))
