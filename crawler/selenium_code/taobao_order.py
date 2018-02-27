# 抓取淘宝个人订单信息
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
# 抓取地址   登录地址
url_dd="https://buyertrade.taobao.com/trade/itemlist/list_bought_items.htm?spm=a21bo.2017.1997525045.2.20d65443RfRxHC"
url_login="https://login.taobao.com/member/login.jhtml"
driver.get("https://login.taobao.com/member/login.jhtml")
time.sleep(5)
# 切换到登录输入窗口
switch_elem=driver.find_element_by_class_name("login-switch")
switch_elem.click()
user_elem=driver.find_element_by_id("TPL_username_1")
pwd_elem=driver.find_element_by_id("TPL_password_1")
sub_elem=driver.find_element_by_id("J_SubmitStatic")
# 输入用户名   在浏览器中输入密码   点击登录
user_elem.send_keys("此处输入淘宝用户名")
print("wait submit")
mstr=input("please input ")
print(mstr)
driver.get(url_dd)
mfile=open(r"1.txt","ab")
print("enter for soon")
# 网站全部内容写入文件
for i in range(1,100):
    time.sleep(10)
    page_one=driver.page_source
    try:
        mfile.write((page_one+"\n==============================================\n").encode("utf-8"))
        print("写入成功")
    except:
        print("写入错误")
    next_elem=driver.find_element_by_xpath("//*[@class=\"pagination-next\"]/a")
    print(next_elem.tag_name)
    print(next_elem.text)
    # 模拟翻页  追踪到该元素时   会被窗口挡住  所以还要向下移动一下
    ActionChains(driver).key_down(Keys.DOWN).perform()
    ActionChains(driver).move_to_element(next_elem).perform()
    time.sleep(1)
    ActionChains(driver).key_down(Keys.DOWN).perform()
    time.sleep(1)
    # 模拟鼠标移动点击释放全过程
    ActionChains(driver).move_to_element(next_elem).click_and_hold(next_elem).release(next_elem).perform()
    print("+++++++++++++++++++++++++++++++++++++",i)
mfile.close()
