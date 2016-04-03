#! uenv/bin/python
#-*-coding:utf8-*-
#从内存中读取str
from io import StringIO,BytesIO

f = StringIO()
f.write("Hello")
f.write(" ")
f.write("wrold!")

#用getvalue获取str

print(f.getvalue())

b = BytesIO()
b.write("中文".encode('utf8'))
print(b.getvalue())