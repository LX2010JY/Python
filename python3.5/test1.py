#! uenv/bin/python3.4
# -*- coding=utf8 -*-

print("Hello World")

#1.可以输出多个字符串，遇到逗号为空格

print('Hello','我是小米','我管你是谁')
name = input("input your name:")
print('Hello ,',name)

#2.转义符
print('I\'m \"OK\"')
print('I\',\t\"OK\"')

#3.格式化
print("hi %s , your score is %d" %('罗霄',100))
