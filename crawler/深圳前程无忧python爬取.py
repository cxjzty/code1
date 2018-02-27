#coding:utf-8
import urllib2
import lxml
import lxml.etree
import re


def jobData(page):
    urlSz = "http://search.51job.com/list/040000,000000,0000,00,9,99,python,2," + str(
        page) + ".html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    # urlSz="http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=040000&keyword=python&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9"
    # urlSz="http://search.51job.com/list/040000,000000,0000,00,9,99,python,2,6.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}
    request = urllib2.Request(urlSz, headers=headers)
    response = urllib2.urlopen(request).read()
    mytree = lxml.etree.HTML(response)
    mlist=[]
    # print sumPageData,type(sumPageData)
    for myline in range(3, 53):
        dataJob = mytree.xpath("//*[@id=\"resultList\"]/div[" + str(myline) + "]//p//span//a//text()")
        dataCompany = mytree.xpath("//*[@id=\"resultList\"]/div[" + str(myline) + "]/span[1]/a/text()")
        dataAddress = mytree.xpath("//*[@id=\"resultList\"]/div[" + str(myline) + "]/span[@class=\"t3\"]/text()")
        dataMoney = mytree.xpath("//*[@id=\"resultList\"]/div[" + str(myline) + "]/span[@class=\"t4\"]/text()")
        dataTime = mytree.xpath("//*[@id=\"resultList\"]/div[" + str(myline) + "]/span[@class=\"t5\"]/text()")
        if len(dataJob) == 0:
            dataJob.append("#")
        if len(dataCompany) == 0:
            dataCompany.append("#")
        if len(dataAddress) == 0:
            dataAddress.append("#")
        if len(dataMoney) == 0:
            dataMoney.append("#")
        if len(dataTime) == 0:
            dataTime.append("#")
        dataJob[0] = dataJob[0].strip()
        mlist.append([dataJob[0],dataCompany[0],dataAddress[0],dataMoney[0],dataTime[0]])
    return mlist
def sumPageData():
    urlSz = "http://search.51job.com/list/040000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}
    request = urllib2.Request(urlSz, headers=headers)
    response = urllib2.urlopen(request).read()
    mytree = lxml.etree.HTML(response)
    sumPageStr=mytree.xpath("/html/body/div[2]/div[6]/div/div/div/span[1]/text()")
    sumPageStr=sumPageStr[0].encode("utf-8")
    pattern="共(.*?)页，到第"
    sumPageData=re.findall(pattern,sumPageStr)[0]
    return sumPageData

if __name__=='__main__':
    # 传入page
    sumPageData =int(sumPageData())
    print sumPageData
    mfile = open("3.txt", "wb")
    for j in range(1,sumPageData+1):
        mlist=jobData(j)
        mstr=""
        for i in mlist:
            mstr+="==".join(i)+"\n"
        mstr=mstr.encode("utf-8")
        mfile.write("===page"+str(j)+"\n")
        mfile.write(mstr)
    mfile.close()






    pass




    # mlist=[]
    # for i in range(len(dataJob)):
    #     mlist.append([dataJob[i], dataCompany[i],dataAddress[i],dataMoney[i],dataTime[i]])
    # mfile=open("小图片.txt","wb")
    # mstr=""
    # for i in mlist:
    #     mstr+=i[0].encode("utf-8")+"=="+i[1].encode("utf-8")+"=="+i[2].encode("utf-8")+"=="+i[3].encode("utf-8")+"=="+i[4].encode("utf-8")+"\n"
    # mfile.write(mstr)
    # mfile.close()
