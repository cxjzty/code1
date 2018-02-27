import os
def get_user(x):
    line=x.decode("utf-8").split("----")[0]
    return line
    pass

block_path = "after_block"
file_list=os.listdir(block_path)
for i in range(len(file_list)):
    file_list[i]=block_path+"/"+file_list[i]
for i in range(len(file_list)):
    input_file=open(file_list[i],"rb")
    output_file_path=block_path+"/sort_"+str(i)+".txt"
    output_file=open(output_file_path,"wb")
    input_file_lines=input_file.readlines()
    input_file_lines.sort(key=lambda x:get_user(x))
    for j in input_file_lines:
        output_file.write(j)
    output_file.close()
    input_file.close()
    print("=============================",i)
