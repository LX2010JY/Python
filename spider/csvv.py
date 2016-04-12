import csv
from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('http://blog.sina.com.cn/u/1245336194')
bsObj = BeautifulSoup(html)
print(bsObj.title.get_text())
blog_title = bsObj.findAll(class_="blog_title")
blog_content = bsObj.findAll(class_="content newfont_family")

for b in blog_title:
    print(b.get_text())





csvFile = open("../file/test.txt",'w+')
try:
    writer = csv.writer(csvFile)
    writer.writerow(('number','number plus 2','number times2'))
    for i in range(10):
        writer.writerow((i,i+i,i*i))
finally:
    csvFile.close()