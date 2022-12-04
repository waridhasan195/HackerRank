# https://www.hackerrank.com/challenges/np-min-and-max/problem?isFullScreen=true


import numpy

n,m = input().split()
list1 = []
for i in range(int(n)):
    list1.append(input().split())
arr = numpy.array(list1,dtype = int)
max_num = numpy.min(arr,axis = 1)
print(numpy.max(max_num))