def merge(one,two,after):
    signal=0
    one_line = one.readline()
    two_line = two.readline()
    while True:
        if one_line.decode("utf-8").split("----")[0] > two_line.decode("utf-8").split("----")[0]:
            after.write(two_line)
            two_line = two.readline()
            if not two_line:
                signal=2
                break
        elif one_line.decode("utf-8").split("----")[0] < two_line.decode("utf-8").split("----")[0]:
            after.write(one_line)
            one_line = one.readline()
            if not one_line:
                signal = 1
                break
        else:
            after.write(one_line)
            after.write(two_line)
            one_line = one.readline()
            two_line = two.readline()
            if not two_line:
                signal=4
                break
            if not one_line:
                signal = 3
                break

    if signal==1:
        while True:
            if two_line:
                after.write(two_line)
            else:
                break
            two_line = two.readline()
    if signal==2:
        while True:
            if one_line:
                after.write(one_line)
            else:
                break
            one_line = one.readline()
    if signal==3:
        while True:
            if two_line:
                after.write(two_line)
            else:
                break
            two_line = two.readline()
    if signal==4:
        while True:
            if one_line:
                after.write(one_line)
            else:
                break
            one_line = one.readline()
    pass
# if __name__=='__main__':
#     one=open("after_block/sort_0.txt","rb")
#     two=open("after_block/sort_1.txt","rb")
#     after=open("after_block/merge01.txt","wb")
#     merge(one,two,after)
#     one.close()
#     two.close()
#     after.close()
