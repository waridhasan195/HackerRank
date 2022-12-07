

# https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true


eng_s_no=input()
roll_eng=set(input().split())
fr_s_no=input()
roll_fr=set(input().split())
result=roll_eng.union(roll_fr)
print(len(result))