from urllib.request import urlopen,Request,urlretrieve
from bs4 import BeautifulSoup
import os
import time
def down(images,title):
    global HEADERS
    j = 0
    dir = '../file/img/'+title
    if not os.path.exists(dir):
        os.makedirs(dir)
    for img in images:
        j = j+1
        name = str(j) + '.jpg'
        img = img.get('src')
        img = img.replace("square","large")
        print(img+"-->"+dir)
        try:
            urlretrieve(img, dir+'/'+name)
        except:
            print('can not download')

HEADERS = {
    "Cookie":"SINAGLOBAL=9378377706167.52.1459581052808; YF-Ugrow-G0=56862bac2f6bf97368b95873bc687eef; YF-V5-G0=b1e3c8e8ad37eca95b65a6759b3fc219; _s_tentry=www.baidu.com; Apache=9871446711305.629.1460533554613; ULV=1460533554671:11:11:3:9871446711305.629.1460533554613:1460507379625; YF-Page-G0=ab26db581320127b3a3450a0429cde69; wb_publish_vip_1788130832=4; login_sid_t=ebab77d3d2b4bb52055ff531aa3c4506; gsid_CTandWM=4umkCpOz5WyT1zoHBmzoo7vaOdq; WBtopGlobal_register_version=ab9111fb56d70a2b; un=luqwedcxsad@sina.cn; SUHB=0KAgwGg89dSZCk; myuid=1788130832; UOR=www.baidu.com,vdisk.weibo.com,login.sina.com.cn; SSOLoginState=1460536623; SUS=SID-1788130832-1460536623-GZ-ts8i7-b3ee258a351e64d62a1c0acaf532c77a; SUE=es%3Dee76f774ad79eeaa47ac7d2cc26a406a%26ev%3Dv1%26es2%3D8ea81c2e1c2daf688c0db9a1d46ccf17%26rs0%3DlczPjc8nqx22hSbMYqB0PQKV889DhqS43mE%252BcalkNzeMU53rUAu%252BeJXBn5HKauquq0BpocSS0QorhPttT%252F0UVuz4pu9n9RQG6U5XQule2XMnMLR44%252Fi1v%252FJ%252BhdMwlEbh2Wx3pZrcv9wWeHlWGp%252BjPpmQF3VR5Gz94KLfPmK%252F51I%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1460536623%26et%3D1460623023%26d%3Dc909%26i%3Dc77a%26us%3D1%26vf%3D%26vt%3D%26ac%3D%26st%3D0%26uid%3D1788130832%26name%3Dluqwedcxsad%2540sina.cn%26nick%3D%25E7%25BB%2583%25E7%25BC%2598%26fmp%3D%26lcp%3D2015-04-19%252011%253A05%253A29; SUB=_2A256CnV_DeRxGedJ41oQ8y7EyD6IHXVZ9Rs3rDV8PEJb6dNAHSGXkm5JFLqo_3dqtJG4eWU8baL7tL_F-7M.; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW4WZjyTH6gV_1VJTUaDWeE",
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 Safari/537.36"
}
weibourl = "http://weibo.cn/album/albummblog/?rl=11&fuid=1353112775&page="
for i in range(1,59):
    url = weibourl+str(i)
    req = Request(url,headers=HEADERS)
    text = urlopen(req).read()
    bsObj = BeautifulSoup(text)
    images = bsObj.findAll('img',{"class":"c"})
    title = str(i)
    down(images,title)

