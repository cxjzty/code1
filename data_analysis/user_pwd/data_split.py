import os
def data_split(length,block):
    length_list=[]
    if length%block==0:
        for i in range(block):
            length_list.append(length//block)
    else:
        s_len=(length-length%block)//(block-1)
        for i in range(block-1):
            length_list.append(s_len)
            length-=s_len
        length_list.append(length)
    return length_list
    pass
if __name__=='__main__':
    qq_file=open("index.txt","rb")
    block_path="after_block"
    split_length=data_split(84319637,10)
    for i in range(len(split_length)):
        small_path=block_path+"/qq"+str(i)+".txt"
        small_file=open(small_path,"wb")
        for j in range(split_length[i]):
            small_file.write(qq_file.readline())
        small_file.close()
        print("=================================",i)
    qq_file.close()