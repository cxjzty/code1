#coding:utf-8
# 模拟登录后载入session后可以使用requests库高效抓取页面
import selenium
import selenium.webdriver
import time
import lxml
import lxml.etree
import requests
driver = selenium.webdriver.Chrome()
driver.get("https://passport.jd.com/new/login.aspx")
time.sleep(3)
elem=driver.find_element_by_xpath("//*[@class=\"login-tab login-tab-r\"]/a")
elem.click()
#切换到账户登录

user=driver.find_element_by_id("loginname")
password=driver.find_element_by_id("nloginpwd")
submit=driver.find_element_by_id("loginsubmit")
user.clear()
password.clear()
time.sleep(1)
user.send_keys("yincheng5201314@163.com")
password.send_keys("yincheng8848")
time.sleep(1)
submit.click()
time.sleep(10) #等待页面加载，
cookies=driver.get_cookies()#抓取全部的cookie
driver.close()

print "开始会话"
req=requests.session()#会话

for  cookie  in cookies:
    req.cookies.set(cookie['name'],cookie["value"])
req.headers.clear()#清空头
newpage=req.get("https://cart.jd.com/cart.action")
print "会话完成"
print newpage.text  #页面
mytree=lxml.etree.HTML(newpage.text  )
print  mytree.xpath("//*[@class=\"cell p-price\"]/strong/text()")

time.sleep(10)

time.sleep(10)
driver.close()














