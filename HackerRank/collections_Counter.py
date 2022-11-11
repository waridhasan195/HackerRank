

from collections import Counter

n = int(input())

stock = list(map(int, input().split()))
print(stock)
dict = Counter(stock)
print(dict)

p = 0

k = int(input())

for i in range(k):
    size, price = map(int, input().split())
    if dict[size]:
        dict[size] -= 1
        p = p+price
print(p)
