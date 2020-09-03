# coding: gbk
print('请在下方输入游戏范围')
fangwe = int(input())
from random import randint
num = randint(1,fangwe)
print('猜猜这个数是几?（不想玩了回-1)')
bingo = False
count = 0

while bingo == False:
    count +=1
    answer = int(input())
    num1 = 10+num
    x = randint(1,10)
    y = randint(1,10)
    z = randint(1,10)

    if answer<num:
        print(str(answer) + '太小了!')
        num = num+x
        
    if answer>num:
        print(str(answer) + '太大了')
        num = num+y
   
    if answer==num1:
        print(str(answer) + '接近了')
        num = num+z

    if answer==-1:
        print(str(num) +  '是正确的答案,游戏失败')
        bingo = True

    if count==100:
        print('游戏失败')
        bingo = True
        
    if answer==num:
        print('答对了,'+ str(answer) +' 是正确的答案')
        bingo = True

print(count)

                

           
           
    
