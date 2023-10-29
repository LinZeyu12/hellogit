'''a=10
#id type value
lst=['hello','world',98]
print(id(lst))
print(type(lst))
print(lst)


print(id('hello'))

'''
'''
#使用内置函数list创建列表
list2=list(['hello','world',98])
print(list2[2])

'''
'''
lst=['hello','world',98,'hello']    #index是获取元素的索引
print(lst.index('hello'))#如果列表中含有相同元素，只返回列表中个第一个元素的索引
#print(lst.index('python'))#如果一个元素不存在，则系统会报错
#print(lst.index('hello',1,3))#不包括第三个数
print(lst.index('hello',1,4))
'''
'''
lst=[20,40,10,98,54] 
print('排序前的列表',lst,id(lst))
#开始排序，调用列表对象的sort方法，升序排序
lst.sort()
print('排序后的列表',lst,id(lst))
lst.sort(reverse=True)     #reverse=True降序
print(lst)
lst.sort(reverse=False)   #reverse=False升序(默认)
print(lst)

lst=[20,40,10,98,54] 
print('原列表',lst)
new_list=sorted(lst)
print(lst)
print(new_list)
desc_list=sorted(lst,reverse=True)
print(desc_list)

'''
'''
lst=[i for i in range(2,11,2)]
print(lst)
'''



'''

scores={'张三':100,'李四':98,'王五':45}
keys=scores.keys()
print(keys)
print(type(keys))
print(list(keys))

print('--------------')
values=scores.values()
print(values)
print(type(values))
print(list(values))
print('--------------')

items=scores.items()
print(items)
print(type(items))
print(list(items))

'''
'''
scores={'张三':100,'李四':98,'王五':45}
for item in scores:
 print(item,scores[item],scores.get(item))


'''
'''
items=['Fruit','Books','Others']
prices=[96,78,85]
d={ item.upper():price for item,price in zip(items,prices) }
print(d)

'''

'''
t=('Python','world',98)
print(t)
print(type(t))

print('------')
t1=tuple(('Python','world',98))
print(t1,type(t1))

'''
t=('Python','world',98)
for item in t:
    print(item)








