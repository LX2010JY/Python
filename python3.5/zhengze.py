#-*- coding:utf8 -*-
import re
# \d表示数字
# \w表示字母
# .表示任意字符
# /////
# *表示[0-无穷]
# +表示[1-无穷]
# ?[0或1]
#[asdasdasddsc213213]表示里面选一个匹配
# {n}表示n个字符
# {n,m}表示n-m个字符
# /////
# [0-9a-zA-Z]匹配一个字母或数字
# 加上^$就只能匹配满足条件的字符串，不加代表只要字符串包含匹配条件就行

a = re.match(r'^\d{3}\-\d{3,8}$','010-12323')
print(a)
b = re.match(r'^\d{3}\-\d{3,8}$','010 12323')
print(b)

str =  'a, b,   c'
print(str.split(' '))

print(re.split(r'[\s+\,]+',str))

#()分组匹配提取
group = 'jia6_yu6@163.com'
g = re.match(r'^(.+)\@(.+)\.com$',group)
print(g.group(1))
print(g.group(2))

#贪婪匹配 向最大极限匹配
num = '123400'
q = re.match(r'^(\d+)(0*)$',num)
print(q.groups())
#加？取消贪婪匹配
num = '123400'
q = re.match(r'^(\d+?)(0*)$',num)
print(q.groups())

aa = "http://www.baidu.com/ashda/resource/book"
#正则查询
print(re.search(r'\/\w+$',aa).group())
#正则替换
link = re.compile("\/\w+$")
info = re.sub(link,'/movie',aa)
print (info)
