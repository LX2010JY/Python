#! uenv/bin/python3.4

#列表生成器

L = []
for i in range(1,10):
    L.append(i*i)
print(L)

ll = [x*x for x in range(1,11) if x % 2 == 0]
print(ll)

ss = [m+n for m in 'ABC' for n in 'XYZ']
print(ss)

dd = {'name':'luoxiao','age':12,'score':34}
print([k+'='+str(v) for k, v in dd.items()])

#生成器 list 不直接生成，而是边循环边生成，节约内存 ， generator

g = (x*x for x in range(100000))
print(next(g))
for n in g:
    print(n)