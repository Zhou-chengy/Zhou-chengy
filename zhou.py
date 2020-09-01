# coding: gbk
from random import randint
num = randint(1,1000)
print('猜猜这个数是几?')
bingo = False
count = 0

while bingo == False:
    count +=1
    answer = int(input())

    if answer<num:
        print(str(answer) + '太小了!')

    if answer>num:
        print(str(answer) + '太大了')

    if answer==num:
        print('答对了,'+ str(answer) +' 是正确的答案')
        bingo = True

print(count)
