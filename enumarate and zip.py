# for key,value in enumerate([1,2,3,4,4]):
#     print(key,':',value)
#
# my_list = ["sandeep",35,"hyderabad"]
# new_list = enumerate(my_list,start=2)
# print (enumerate(my_list,start=2))
#
# for newlist_item in new_list:
#     print(newlist_item)
#
#
# #zip functionality
# my_keys_list = ["name","age","location","pin"]
# mylist = ["sandeep",35,"hyderabad"]
# mynewlist = zip(my_keys_list,mylist)
# for key,value in mynewlist:
#     print(key,value)

#iterateitems only on dict
#
# mydict = {"name":"sandeep","age":35,"location":"hyderabad"}
# for item in mydict.items():
#     print(item)
# for key,value in mydict.items():
#     print(key,value)

#looping using sorted

mylist = [1,2,4,1,2,3,2,4,5,6,3,3,4]
mysortedlist = sorted(mylist)
print(mylist)
print(mysortedlist)
print(set(mysortedlist))
print(sorted(set(mylist)))
print(list(range(10)))
print(list(range(0,10,3)))
print(list(reversed(range(0,10,3))))