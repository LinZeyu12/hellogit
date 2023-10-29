
'''
a=1
#判断条件表达式
while a<10:
    print(a)
'''

'''
#计算0-4之间的累加和
#四步循环法  1.初始化变量 2.条件判断 3.条件执行体 4.改变变量

a=0
he=0
while a<=4:
     he+=a
     a+=1
     print(he)

'''


'''
#1到100的偶数和
number=1
he=0
while number<=10:
      if number%2==0:
         he+=number
         number+=1
print(he)
'''
'''
for item in 'Python':
  print(item)


for number in range(10):
 print(number)
#如果在循环体中不需要使用到自定义变量，可以将自定义变量写为“_”，此时range代表循环次数
for _ in range(5):
    print('21365')
'''

'''



he=0
for i in range(101):
    if not bool(i%2):
       he+=i
print(he)

'''

'''

print('输出100到999之间的水仙花数')
#举例153=3*3*3+5*5*5+1*1*1
for item in range(100,1000):
    
 ge=item%10  #得到个位上的数
 shi=(item%100)//10   #得到个位上的数
 bai=item//100   #得到个位上的数
 #print(bai,shi,ge)
 #判断
 if ge**3+shi**3+bai**3==item:
  print(item)

'''


'''
for _ in range(3):
    
 pwd=int(input('请输入密码：'))
 if pwd==8888:
     print('密码正确')
     break
 else:
     print('密码错误')
'''


'''
a=0
while a<3:
 pwd=int(input('请输入密码：'))
 if pwd==8888:
    print('密码正确')
    break
 else:

    print('密码错误')

'''

'''
#要求输出1-50之间所有5的倍数
for number in range(1,51):
    if number%5==0:
     print(number)

print('-----------使用continue----')
for item in range(1,51):
    if item%5!=0:
        continue
    print(item)        
'''

'''
for item in range(3):
    pwd=int(input('请输入密码：'))
    if pwd==8888:
        print('密码正确')
        break
    else:
        print('密码错误')
else:    #for循环执行完，且过程中没有遇到break，则执行else
    print('对不起，三次输入都错误')

'''

'''
a=0
while a<3:
    pwd=int(input('请输入密码：'))
    if pwd==8888:
        print('密码正确')
        break
    else:
        print('密码错误')
        a+=1
else:
    print('三次密码都输错了')
'''

'''
print('-------嵌套循环-------')
#输出三行四列的矩形
for i in range(3):
    for j in range(4):
        print('*',end='\t')
    print()
    
'''
'''
print('----九九乘法表-----')
for i in range(10):
 for j in range(1,i+1):
   print(j,'*',i,'=',i*j,end='  ')
 print()
   
   '''


for i in range(5):   #外层循环的个数
    for j in range(1,11):
        if j%2==0:
            continue
        print(j,end='\t')
           # break
    print()






