

n, m = map(int, input().split())


array = list(map(int, input().split()))


A = set(map(int, input().split()))
B = set(map(int, input().split()))


if m == len(A) and m == len(B):
    if len(array) == n:
        print(sum((i in A) - (i in B) for i in array))
        print("Success")
    else:
        print("Error")
else:
    print("Total Error")