

# word = 'BANANA'

# word_lenth = len(word)
# substring_lenth = 1

# for i in range(word_lenth):
#     for j in range(i+1, word_lenth+1):
#         print(word[i:j])


S = str(input())


StuartScore, KevinScore = 0, 0

for i in range(len(S)):
    if S[i] in ["A", "E", "I", "O", "U"]:
        KevinScore = KevinScore + len(S) - i
    else:
        StuartScore += len(S) - i

if KevinScore > StuartScore:
    print("Kevin", KevinScore)
elif KevinScore < StuartScore:
    print("Stuart", StuartScore)
else:
    print("Drow")
