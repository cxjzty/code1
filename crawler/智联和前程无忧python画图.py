#encoding:utf-8
import urllib2
import lxml.etree
import re
import matplotlib
import matplotlib.pyplot as plt


def loadJobNum(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request).read()
    mytree = lxml.etree.HTML(response)
    datalist = mytree.xpath("//*[@id=\"resultList\"]/div[1]/div[3]/text()")
    dataStr = datalist[0].strip().encode("utf-8")
    pattern = "共(.*?)条职位"
    dataNum = re.findall(pattern, dataStr)
    return dataNum[0]


def jobData():
    # 深圳
    urlSz = "http://search.51job.com/list/040000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    dataSz = loadJobNum(urlSz)
    # 上海
    urlSh = "http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=020000&keyword=python&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9"
    dataSh = loadJobNum(urlSh)
    # 北京
    urlBj = "http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=010000&keyword=python&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9"
    dataBj = loadJobNum(urlBj)
    # 杭州
    urlHz = "http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=080200&keyword=python&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9"
    dataHz = loadJobNum(urlHz)
    return ["job",dataBj,dataSh,dataHz,dataSz]
def zhaopin(url):
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}

    request=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(request).read()
    mytree=lxml.etree.HTML(response)
    dataWeb=mytree.xpath("/html/body/div[3]/div[3]/div[2]/span[1]/em/text()")
    return dataWeb


def zhaopinData():
    # 深圳
    dataSz = str(zhaopin("http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw=python&sm=0&p=1")[0])
    # 上海
    dataSh = str(
        zhaopin("http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E4%B8%8A%E6%B5%B7&kw=python&p=1&isadv=0")[0])
    # 北京
    dataBj = str(
        zhaopin("http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python&p=1&isadv=0")[0])
    # 杭州
    dataHz = str(
        zhaopin("http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%9D%AD%E5%B7%9E&kw=python&p=1&isadv=0")[0])
    return ["zhaopin",dataBj,dataSh,dataHz,dataSz]


def draw(data):
    matplotlib.rcParams["font.sans-serif"] = ["simhei"]
    matplotlib.rcParams["font.family"] = "sans-serif"
    for i in range(1, len(data)):
        data[i] = int(data[i])
    plt.bar([1], [data[1]], label=u"北京")
    plt.bar([2], [data[2]], label=u"上海")
    plt.bar([3], [data[3]], label=u"杭州")
    plt.bar([4], [data[4]], label=u"深圳")
    plt.legend()
    plt.show()


if __name__=='__main__':
    draw(jobData())


    pass






