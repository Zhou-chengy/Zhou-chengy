# coding: gbk
from random import randint
num = randint(1,1000)
print('�²�������Ǽ�?')
bingo = False
count = 0

while bingo == False:
    count +=1
    answer = int(input())

    if answer<num:
        print(str(answer) + '̫С��!')

    if answer>num:
        print(str(answer) + '̫����')

    if answer==num:
        print('�����,'+ str(answer) +' ����ȷ�Ĵ�')
        bingo = True

print(count)
