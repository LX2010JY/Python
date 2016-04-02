#! uenv/bin/python3.4
# -*-coding:utf8 -*-

# list 列表 类似数组
array = []
item = []
for i in range(10):
    for j in range(3):
        item.append(j)
    array.append(item)
    item = []
print(array)
#insert 添加
array.insert(1,'asdasd')
print(array)
#pop 删除 append 添加
array.pop(1)
print(array)

#tuple() 类似list 但是tuple只能在初始化时定义，后面不能修改，更安全。
t = (1,2,3,'12',4,[1,2,3])
#在只有一个元素时，要在后面加逗号，否则tuple会被当成括号
a = (1,)
print(t,a)

#if else elif 条件判断 和 循环
array = []
item = []
for i in range(1,13):
    print ("i = %d , i/3=%d" % (i,i % 3))
    if i%3 !=0:
        item.append(i)
    else:
        item.append(i)
        array.append(item)
        item = []

print(array)

#dict 和 set

# 和list比较，dict有以下几个特点：
#
# 1.查找和插入的速度极快，不会随着key的增加而变慢；
# 2.需要占用大量的内存，内存浪费多。
# 而list相反：
#
# 1.查找和插入的时间随着元素的增加而增加；
# 2.占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。
# 这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。

#dict 字典 java中叫map 也就是 键值对,键值对的查询速度很快，优于list
print('<-------------------键值对---------------------->')
d = {'luoxiao':90,'jiayu':100,'ziyue':'99'}
print(d)
d['haha'] = 90
d['wuwu'] = 78
d['gaga'] = 27
print(d,"d['luoxiao'] = %d" % d['luoxiao'])
#print(d['asdjsh']),key 不存在，报错，所以必须换种方式
d.pop('gaga')
print(d)
key = input('输入key:')
if key in d:
    print(d[key])
else:
    print('%s 不存在于dict中'% key)


#set 初始化时以list

s = set([1,2,3])
print(s)
s.add(23)

print(s)