
# https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true

from itertools import product


# --------------
#product
# a = [1,2,3]
# b = [4,5,6]
# c = list(product(a, b, repeat=2))
# print(c)

# d = list(product(a, repeat = 2))
# # print(d)
# --------------

# ----------------
# Map
# number = [2, 4, 6, 8, 10]
# def Squere(x):
#     return x*x
# print(list(map(Squere, number)))
# ----------------

# ----------------
# lamda 
# number = [2, 4, 6, 8, 10]
# result = list(map(lambda x: x*x, number))
# print("Lambda: ", result)
# ----------------


# a = [1, 2]
# b = [3, 4]

# result = tuple(map(lambda x, y:  a, b))
# print(result)


# from itertools import sum as p

# A=map(int,input().split())
# B=map(int,input().split())    
# print(p(A,B))




# a = [int (x) for x in input().split()]
# b = [int (x) for x in input().split()]
# print(a)
# print(b)


from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

x = list(product(a, b))
result = ''
for i in x:
    a = str(i)
    result = result + " " + a

print(result)

