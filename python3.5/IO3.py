#! uenv/bin/python
import pickle
#序列化输入
d = dict(name="luoxiao",age=12,score=99)
f = open("test",'wb')
pickle.dump(d,f)
f.close()

#反序列读取
f = open("test",'rb')
d = pickle.load(f)
f.close()
print(d)
