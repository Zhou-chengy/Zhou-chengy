# coding: gbk
from random import randint
num = randint(1,1000)
print('�²�������Ǽ�?���������˻�-1)')
bingo = False
count = 0

while bingo == False:
    count +=1
    answer = int(input())
    num1 = 10+num

    if answer<num:
        print(str(answer) + '̫С��!')
        num = num+10
        
    if answer>num:
        print(str(answer) + '̫����')
        num = num+5
   
    if answer==num1:
        print(str(answer) + '�ӽ���')
        num = num+6

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

                

           
           
    
