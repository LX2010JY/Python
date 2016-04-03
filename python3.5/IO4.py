import json

class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
    }
s  = Student('Bob',12,89)
print(json.dumps(s,default=student2dict))

#json写入文件
j = {'name':'fjiayu','age':15,'score':99}
json.dump(j,open('test','w'))
#json 读取json
f = open('test','r')
print(json.load(f))

