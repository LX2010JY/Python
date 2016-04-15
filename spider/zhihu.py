from bs4 import BeautifulSoup
import time
from urllib.request import urlopen,Request
from selenium import webdriver

header = {
    "Cookie":'d_c0="AAAA9oPxtQmPTgZSyN7p-gTBmwqPwnplUiQ=|1459608840"; q_c1=ddfd4b93b84c40e5bff890da799bfe91|1459608840000|1459608840000; _za=1988f9a3-7934-4d94-8f8c-b7644246653b; _ga=GA1.2.370817364.1460126283; __utma=51854390.370817364.1460126283.1460468652.1460468652.1; __utmz=51854390.1460468652.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.000--|3=entry_date=20160402=1; _xsrf=63ea9ec823484c1fd2b0c9c5de4069f7; _zap=61585b8b-a399-4b4e-a0a8-339fc02880f6; l_cap_id="YWE0NTNmODZhMjAyNGJiODgwNTJjZjRmYmM3YmJmZjg=|1460597739|fce3b52b2490ce53422accea6a720e971c449315"; cap_id="Y2YxNjI1M2JmNjJhNGFjMjljNGM1NmM5MmQ1MzI4ZDk=|1460597739|b5c790e0283d7fad9d01e28ca91ea9d2bb183bce"; login="NDQyMTI1MjY3MTY2NDA4NGI4MGE2OGE1NGJhOWQ4NDE=|1460597779|4c49cd5e8c9d80b6ad77f3cc3a565ad42cc86419"; z_c0="QUJBQU53RDc5d2NYQUFBQVlRSlZUUXlDTmxjWFhCQWJoSEd6UGI2eExJMjZPZ2ZSUlBEODJRPT0=|1460598028|facf580e5f3640300cb499fa898632fe72657a71"; unlock_ticket="QUJBQU53RDc5d2NYQUFBQVlRSlZUUlQ4RGxmdkYxeWl5Qmc5MWdqX2NYS000ZmtySjFzbUZnPT0=|1460598028|ebda6dd22456be6208cc3b74a300156c3a83adfd"; n_c=1',
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 Safari/537.36"
}
request = Request('https://www.zhihu.com/topic',headers=header)
html = urlopen(request)
bsObj = BeautifulSoup(html)
question = bsObj.findAll('a',{"class":"question_link"})
for qus in question:
    print(qus.get_text())
    time.sleep(1)

driver = webdriver.Firefox()
driver.get("http://www.zhihu.com/#signin")
driver.find_element_by_name("account").clear()
driver.find_element_by_name("account").send_keys('jia6_yu6@163.com')
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys('jia6yu6')
driver.find_elements_by_tag_name('button')[1].click()

time.sleep(2)
print(driver.page_source)
print(driver.find_element_by_class_name("name").text)



