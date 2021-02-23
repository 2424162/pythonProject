import re
file = "xposed344.log"
file2 = "URL.log"
file3 = "host.log"
file4 = "host1.log"
path = "zuihou/"



def url_inspectors(): #筛选url

    num = 0
    f = open(file,"rb+")
    f2 = open(path+file2,"a+");
    for i in f.readlines():
        print(i)
        if "URL =".encode("utf-8") in i:
            f2.write(i.decode("utf-8"))
            num = num + 1
    print(num)


def host_inspectors(): #筛选host
    f2 = open(path+file2,"r+")
    host_set = set()
    for i in f2.readlines():
        host_pat = "URL = (https://.*?)/"

        host = re.findall(host_pat,i)
        if(len(host)>0):
            print(host[0])
            host_set.add(host[0])
    print(host_set)
    return host_set

def write_host(hosts): #写入 host
    f3 = open(path+file3,"a+")
    for i in hosts:
        f3.write(i+ "\n")

def write_sort_host(hosts):  # 写入 排序host
    host_list = list(host_set)
    host_list.sort()

    f4 = open(path+file4, "a+")
    for i in host_list:
        f4.write(i + "\n")

url_inspectors()
host_set = host_inspectors()
#write_host(host_set)
write_sort_host(host_set)



