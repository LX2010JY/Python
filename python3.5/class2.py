#! uenv/bin/python3.4
# -*- coding:utf8 -*-
from types import MethodType

class Animal(object):
    #类似静态方法，类不用实例化也可以访问，所有对象皆可访问
    name = 'Luoxiao'
    __slots__ = ('__name','__age','__score','email','phone')
    def __init__(self,name='luoxiao',age=12,score=90):
        self.__name = name
        self.__age = age
        self.__score = score

    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_score(self):
        return self.__score

    def set_name(self,name):
        self.__name = name
    def set_age(self,age):
        self.__age = age
    def set_score(self,score):
        self.__score = score

    def run(self):
        print("Animal is running")

class Cat(Animal):
    def run(self):
        print("cat is running")

class Dog(Animal):
    def run(self):
        print('Dog is running')

if __name__ == '__main__':
    a = Animal('luoxiao',13,19)
    a.run()

    d = Dog()
    d.run()
    print(Animal.name,a.name,d.name,isinstance(d,Animal))

    def add(self):
        print('我是添加的方法.')

    #添加方法
    Animal.add = MethodType(add,Animal)
    d.add()
    #添加属性
    d.haha = 'asldjbh'
    print(d.haha)

