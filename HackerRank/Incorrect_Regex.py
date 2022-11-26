
# https://www.hackerrank.com/challenges/incorrect-regex/problem?isFullScreen=true


import re

for each in range(int(input())):
    try:
        P = re.compile(input())
        print(True)
    except re.error:
        print(False)


        