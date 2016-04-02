#! uenv/bin/python3.4

# function
#计算平方
# def power(x):
#     return x*x
#
# print(power(3))
#计算n次方,n默认为2可以不填,必选参数在前，默认参数在后

def power(x,n=2):
    s = 1
    while n>0:
        n = n-1
        s = s * x
    return s

print("5的平方:%s"%power(5))
print("4的10次方:%s"%power(4,10))


#可变参数 num1 以list 或 tuple 输入：

def cacl(number):
    sum = 0
    for num in number:
        sum = sum + num*num
    return sum

print(cacl([1,2,3]))

#num2 *number 自动将参数组装成tuple:
def aaa(*number):
    sum = 0
    for n in number:
        sum = sum + n * n
    return sum

print(aaa(1,2,3,4,4))
l = [1,2,3,4,5]
#list前面加*可以作为可变参数传入
print(aaa(*l))

#关键字参数 **key 自动封装为dict字典

def ddd(name,age,**key):
    return("name:",name,"age",age,"other",key)

print(ddd('luoxiao',12,city="sichuan"))

#这里和上面的可变参数是一样的
extra = {'email':'2810752073@qq.com','phone':'18811409281'}
print(ddd('luoxiao',12,**extra))


#递归

def fact(n):
    if n ==1 :
        return 1
    else:
        return n* fact(n-1)

print(fact(5))