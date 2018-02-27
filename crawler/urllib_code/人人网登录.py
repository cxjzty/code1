# coding:utf-8

import urllib
import  urllib2
import cookielib
#创建一个对象存储cookie
cookie=cookielib.CookieJar()
#创建一个链接对象使用cookie
cookie_handler=urllib2.HTTPCookieProcessor(cookie)
opener=urllib2.build_opener(cookie_handler) #打开器，使用cookie
#增加一个浏览器模拟
opener.addheaders=[("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")]
loginurl="http://www.renren.com/PLogin.do"
data={"email":"账号","password":"密码"}
data=urllib.urlencode(data) #编码
request=urllib2.Request(loginurl,data=data)#post请求登陆，抓取cookie
response=opener.open(request)#载入cookie,登陆
response_index=opener.open("http://www.renren.com/242245656/profile")
print response_index.read()

