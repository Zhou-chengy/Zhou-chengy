# coding: gbk
print('�����·�������Ϸ��Χ')
fangwe = int(input())
from random import randint
num = randint(1,fangwe)
print('�²�������Ǽ�?���������˻�-1)')
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
        print(str(answer) + '̫С��!')
        num = num+x
        
    if answer>num:
        print(str(answer) + '̫����')
        num = num+y
   
    if answer==num1:
        print(str(answer) + '�ӽ���')
        num = num+z

    if answer==-1:
        print(str(num) +  '����ȷ�Ĵ�,��Ϸʧ��')
        bingo = True

    if count==100:
        print('��Ϸʧ��')
        bingo = True
        
    if answer==num:
        print('�����,'+ str(answer) +' ����ȷ�Ĵ�')
        bingo = True

print(count)

                

           
           
    
