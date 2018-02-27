filepath="index.txt"
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

while True:
    linenum=eval(input("input lines"))
    myinputfile.seek(lengthlist[linenum-1],0) #跳到某一行的位置
    line=myinputfile.readline()#读取1行
    print(line)

myinputfile.close()
