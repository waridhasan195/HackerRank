

# https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true


# import collections

# n = int(input())

# value = list(input().split())
# print(value)

# unicword = list(set(value))
# print(len(unicword))

# count = 0


# result = collections.Counter(unicword)
# print(result)




from collections import Counter
word = list(input() for _ in range (int(input())))
print(len(Counter(word)))
print(*Counter(word).values())
 