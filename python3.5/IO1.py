#! uenv/bin/python3.4
#-*-coding:utf8 -*-

# open 打开文件 r 代表读
try:
    f = open("../README.md",'r')
    print(f.read())
finally:
    if f:
        f.close()

#打开文件必须关闭，但是可以用以下方式

with open("../README.md",'r') as f:
    print(f.read())

#read(size)
print('<----------3-------->')
with open("../README.md",'r') as f:
    print(f.read(12))
    print(f.read(12))

#readline()
print('<---------4-------->')
with open("../README.md",'r') as f:
    print(f.readline())

#readlines()
print('<---------5-------->')
with open("../README.md",'r') as f:
    ff = f.readlines()
    for i in ff:
        print(i)


#打开二进制图片 如图片
print('<---------6-------->')
with open("mn.jpg",'rb') as f:
    ff = f.read()
    print(ff)
    #16进制显示

#写入
with open("test",'w',encoding='utf8') as f:
    f.write("你好,中国")
