# https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true



from itertools import permutations

input_data_text, input_data_amount = list(map(str, input().split()))
input_data_text = sorted(input_data_text)
input_data_amount = int(input_data_amount)


for i in permutations(input_data_text, input_data_amount):
    print(''.join(i))
