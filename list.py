# print ("Hello World!")
# print ("Hello Again")
# print ("I like typing this.")
# print ("This is fun.")
# print ("Yay! Printing.")
# print ("I'd much rather you 'not'.")
# print ('I "said" do not touch this.')
import this

data = ['Imac','imax','smsung galaxy',(2010,8,31)]
x,y,z,d = data
print (x)
print(y)
print(z)
print(d)
a,b,c = d
print (a,b,c)

#*号可以代替多个变量，输出的时候变量名不加*号，这是2.7版本不能执行的
#others 永远都是列表类型，即使0个.
name,email,*others = data
print (others)

#获取可迭代对象元素的第一个和最后一个变量函数
def get_first_last(grades):
	first,*middle,last = grades
	return avg(middle)
def avg(number):
	return(sum(number)/len(number))

grades = [43,54,76,89,56,345]
print(get_first_last(grades))