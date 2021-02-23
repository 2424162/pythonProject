import time

list1 =[1,2,1,3,5,6,5,7,6,1]


def set_list():
    len = len(list1)
    list2 =set()
    for i in range(0,len):
        for j in range(i+1,len) :
            if(list1[i]==list1[j]):
                print(list1[i])
def time_sum(fun):
    def wapper(*args ,**dargs):
        start = time.time()
        cc = fun(*args,**dargs)
        print('xixi')
        end = time.time()
        ti  = end -start
        print(ti)
        return cc
    return wapper
def sort_1():
    len = len(list1)
    dict1 ={}
    for i in range(0,len):
        count = 1

        for j in range(i+1,len):
            if list1[i] == list1[j]:
                count =count+1
        print(count)
        if list1[i] not in list(dict1.keys()) :
                dict1[list1[i]] = count

    print(dict1)
    a = sorted(dict1.items(),key=lambda  x:x[1],reverse=True)
    print(a)

@time_sum
def add(str1,str2):
    str1 = str1
    print("haha")


str1 = "123123"
str2 = "234324"
add(str1,str2)
