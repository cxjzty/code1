# 对抓到的整个页面进行内容提取，写入mysql数据库
import lxml.etree
import pymysql
mfile=open("1.txt","rb")
mstr=mfile.read().decode("utf-8")
mfile.close()
mlist=mstr.split("==============================================")
conn=pymysql.connect(host="127.0.0.1",port=3306,user="root",password="root",
                     database="t1",charset="utf8"
                     )
cursor=conn.cursor()
thing_name=[]
thing_money=[]
thing_date=[]
for j in mlist:
    mytree=lxml.etree.HTML(j)
    for i in range(4,19):
        date_xpath="//*[@id=\"tp-bought-root\"]/div["+str(i)+"]/div/table/tbody[1]/tr/td[1]/label/span[2]/text()"
        name_xpath= "//*[@id=\"tp-bought-root\"]/div[" + str(i) + "]/div/table/tbody[2]/tr[1]/td[1]/div/div[2]/p[1]/a[1]/span[2]/text()"
        money_xpath="//*[@id=\"tp-bought-root\"]/div["+str(i)+"]/div/table/tbody[2]/tr[1]/td[5]/div/div[1]/p/strong/span[2]/text()"
        try:
            temp_name=mytree.xpath(name_xpath)[0]
            temp_money=mytree.xpath(money_xpath)[0]
            temp_date=mytree.xpath(date_xpath)[0]
        except (IndexError,AttributeError) as e:
            temp_name= "#"
            temp_money="#"
            temp_date="#"
        thing_name.append(str(temp_name))
        thing_money.append(str(temp_money))
        thing_date.append(str(temp_date))
for i in range(len(thing_name)):
    cursor.execute('insert into taobao2(name,money,date) values("%s","%s","%s")'%(thing_name[i],thing_money[i],thing_date[i]))
cursor.close()
conn.commit()
conn.close()


