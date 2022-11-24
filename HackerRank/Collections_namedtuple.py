

# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true


from collections import namedtuple

N = int(input())
Students = namedtuple('Students', list(input().split()))
total_marks = 0

for _ in range(N):
    student = Students(*input().split())
    total_marks += int(student.MARKS)
print("{:.2f}".format(total_marks/N))


