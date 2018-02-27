
def search2(searchstr,lengthlist):
    low = 0  # 第一个
    high = len(lengthlist) - 1  # 代表最后一个

    times = 0
    while low <= high:  # 不能重叠
        times += 1
        print("times", times)
        mid = (low + high) // 2  # 取出中间索引

        midindex=lengthlist[mid] #取出位置，
        myinputfile.seek(midindex,0) #移动到位置
        line=myinputfile.readline() #读取以行
        line=line.decode("gbk","ignore") #解码
        linelist=line.split(" # ")#切割
        middata=linelist[0] #挖出user,按照user

        if searchstr< middata:  # 小于 淘汰1半
            high = mid - 1
        elif searchstr > middata:  # 小于 淘汰1半
            low = mid + 1
        else:
            print("find", line, mid)
            return mid
    print("not find")
    return -1


filepath="my.txt"
myinputfile=open(filepath,"rb")
mylist=myinputfile.readlines()


lengthlist=[0]
for  line in mylist:
    lengthlist.append(len(line)) #读取每一行的长度到数组


i=0
length=len(lengthlist)
while i <length -1:
    lengthlist[i+1]+=lengthlist[i] #叠加，确定每一行的文件位置
    i+=1
print("索引生成了")

while True:
   searchstr=input("input data")
   search2(searchstr,lengthlist)

myinputfile.close()