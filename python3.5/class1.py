#! uenv/bin/python3.4
# -*-coding： utf8 -*-
#面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。
import sys
__author__ = 'luoxiao'

class Student(object):
    def __init__(self,name,age,score):
        self.__name = name
        self.__age = age
        self.__score = score

    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def get_age(self):
        return self.__age
    def set_name(self,name):
        self.__name = name
    def set_age(self,age):
        self.__age = age
    def set_score(self,score):
        self.__score = score

    def show(self):
        print("name:",self.__name,'age:',self.__age,'score:',self.__score)


    def test(self):
        print (sys.argv)
#继承
class middleschool(Student):
       pass


#这句话表示如果这个文件是被直接运行则执行，否则被其他文件调用就不执行
if __name__ == '__main__':
    stu = Student('luoxiao',12,99)
    stu.show()
    name = input('输入你想修改的名字：')
    stu.set_name(name)
    stu.show()
    mid = middleschool('luoxiao',12,12)
    mid.test()
    #判断 对象是什么类型，mid继承Student 所以依然为True
    print(isinstance(mid,Student))
    #获取对象所有方法和属性
    print(dir(mid))