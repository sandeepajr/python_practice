def print_list(value,l=[]):
    l.append(value)
    return l
list1=print_list(10)
list2=print_list(123,[])
list3=print_list('a')
print(list1)
print(list2)
print(list3)
print(list1,list2,list3)


def print_list(mylist):
    mylist = [12,13]
    # mylist.append(10)

mylist = [1,2,3,4]
print_list(mylist)
print(mylist)
# print(print_list)

a = 10
b = 20
a,b = b,a


a= a+b
b=a-b
a= a-b

# prin 1-100 without loops
# recurvissive

def print_100(i):
    print(i)
    i+=1
    if i !=101:
        print_100(i)
print_100(0)


import re
str1 = "ABCDCDC"
str2 = "CDC"
print(re.findall(str2,str1))

# find the second  maximum number
list1=[1,6,9,1,12,11,30,50,3,5]
# list1.sort()
list2 = list(set(list1))
print(list2.sort())
print(list2)
print(list2[-2])
# list2.sort()
# print(list2[1])
# print(list2[1])