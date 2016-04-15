from urllib.request import Request,urlopen
from urllib.parse import urlencode
url = "http://www.10rain.site/weixin/index.php/Admin/Index/check"

values = {
    'email':'admin',
    'password':'123456',
}
aa = urlencode(values)
aa =  aa.encode(encoding='UTF-8')
print(aa)
data = Request(url,aa)
response = urlopen(data)
print(response)
the_page = response.read()
print(the_page)