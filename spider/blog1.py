from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import os

def findList(url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html)
    print(bsObj.title.get_text())
    blog_title = bsObj.findAll(class_="blog_title")
    for b in blog_title:
        url = b.a.get('href')
        findImage(url)

def findImage(url):
    print(url)
    html = urlopen(url)
    bsObj = BeautifulSoup(html)
    try:
        content = bsObj.find(class_="articalContent")
        images = content.findAll('img')
        title = bsObj.find(class_='articalTitle').find('h2').get_text()
        dir = '../file/img/'+title
        if not os.path.exists(dir):
            os.makedirs(dir)
        for img in images:
            name = str(img.get('name'))+'.jpg'
            imgurl = img.get('real_src')
            print(imgurl+'图片正在下载中....')
            urlretrieve(imgurl,dir+'/'+name)
    except:
        print('格式不对')



# url = "http://blog.sina.com.cn/s/blog_4a3a528201017njb.html"
# findImage(url)

url = 'http://blog.sina.com.cn/u/1245336194'
findList(url)