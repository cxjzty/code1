from file_merge import merge
def merge_all_fun(path_one,path_two,path_after):
    if path_two=="after_block/sort_10.txt":
        return
    one = open(path_one, "rb")
    two = open(path_two, "rb")
    after = open(path_after, "wb")
    merge(one, two, after)
    print("========================已排完",path_one,"++",path_two,"++",path_after)
    one.close()
    two.close()
    after.close()
    global j
    j += 1
    path_two_plus = "after_block/sort_" + str(j) + ".txt"
    path_after_plus = "after_block_1/merge0-" + str(j) + ".txt"
    merge_all_fun(path_after,path_two_plus,path_after_plus)
if __name__=='__main__':
    i=0
    j=1
    path_one = "after_block/sort_" + str(i) + ".txt"
    path_two = "after_block/sort_" + str(i + 1) + ".txt"
    path_after = "after_block_1/merge0-"+ str(i + 1) + ".txt"
    merge_all_fun(path_one,path_two,path_after)
    pass