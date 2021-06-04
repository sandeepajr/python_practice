# #practice of lists
#
# mylist = [1,2,3,"sandeep",3.2]
# print(len(mylist))
#
# mylist.append(22)
# print(mylist)
# mylist.insert(3,"ram")
# print(mylist)
# mylist.insert(15,"ram")
# print(mylist)
# mylist2 = ["amp","East godavari","ram"]
#
# mylist.extend(mylist2)
# print(mylist)
# mylist.remove("ram")
# print(mylist)
# print(mylist.count("ram"))
# deleted_item = mylist.pop(2)
# print(deleted_item)
# print(mylist)
#
# index= mylist.index("ram")
# print(index)
#
# mylist = [1,2,3,1,2,5,32,42,2,3]
# print(mylist.sort())
# print(mylist)
#
# mylist.reverse()
# print(mylist)

import copy
mylist1 = [1,2,3,4,5,6]

mylist2 = mylist1
mylist3 = mylist1.copy()
mylist4 = copy.deepcopy(mylist1)

mylist1.append("ram")
mylist1.insert(2,"sandeep")

print(mylist1)
print(mylist2)
print(mylist3)
print(mylist4)


mylist = list(map(int,input("enter list").split()))
print(mylist)

a,b,c,d = mylist
print(a,b,c,d)