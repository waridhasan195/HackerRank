# https://www.hackerrank.com/challenges/hex-color-code/problem?isFullScreen=true

import re
pattern = r'''(?!^)(#[a-f\d]{3}|#[a-f\d]{6})\b(?!$)'''
regex = re.compile(pattern, flags=re.I)
for each in range(int(input())):
    if founds:=regex.findall(input()):
        print(*founds, sep='\n')