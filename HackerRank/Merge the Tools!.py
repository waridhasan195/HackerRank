def merge_the_tools(string, k):
    segment = ''

    for i in range(len(string)):
        if string[i] not in segment:
            segment += string[i]

        if (i+1)%k == 0:
            print(segment)
            segment = ''


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)