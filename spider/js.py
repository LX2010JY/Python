from selenium import webdriver
import time
from bs4 import BeautifulSoup

# driver = webdriver.PhantomJS()
# driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
# time.sleep(3)
#
# print(driver.find_element_by_id('content').text)
# driver.close()
start = time.time()
browser = webdriver.Firefox()
browser.get('http://www.baidu.com')
print ('现在将浏览器最大化')
browser.maximize_window()

browser.find_element_by_id('kw').send_keys(u'杨彦星')
end = time.time()
print("use time:"+str(end-start))
print (browser.find_element_by_id('kw').get_attribute('type'))
print (browser.find_element_by_id('kw').size) #打印输入框的大小
browser.find_element_by_id('su').click()
aaa = browser.page_source
bsObj = BeautifulSoup(aaa).findAll('div',{'id':'page'})
print(bsObj)