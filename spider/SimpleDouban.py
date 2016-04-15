from urllib.request import urlopen,urlretrieve
from bs4 import BeautifulSoup

# flag = 0
# url = "https://movie.douban.com/top250?start="
# html = urlopen(url)
# for i in range(0,10):
#     top = url+str(i*25)
#     html = urlopen(top)
#     bsObj = BeautifulSoup(html)
#     infos = bsObj.findAll('div',{'class':'item'})
#     for info in infos:
#         msg = info.find('a').find('img')
#         name = msg.get('alt')
#         src = msg.get('src')
#         flag = flag + 1
#         print (str(flag)+" : "+name+"  "+src)
#         urlretrieve(src,'../file/img/douban-Top250/'+name+".jpg")
#
#

flag = 0
url = "https://movie.douban.com/top250?start="
html = urlopen(url)
for i in range(0,10):
    top = url+str(i*25)
    html = urlopen(top)
    bsObj = BeautifulSoup(html)
    infos = bsObj.findAll('div',{'class':'info'})
    for info in infos:
        movie_name = ''
        msg = info.find('a').findAll('span')
        for m in msg:
            movie_name = movie_name + m.get_text()
        flag = flag + 1
        print(str(flag) + " : ")
        print ('movie_name:'+movie_name)
        star = info.find('span',{'class':'rating_num'})
        print('star:'+star.get_text())
        print('---------------------------------------------')

