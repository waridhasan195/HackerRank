

def average(array):
    set_array = set(array)
    array_len = len(set_array)
    array_sum = 0
    result_avg = 0
    for i in set_array:
        array_sum += i
    result_avg = (array_sum/array_len)
    result_avg = f'{result_avg:.3f}'
    return result_avg



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)