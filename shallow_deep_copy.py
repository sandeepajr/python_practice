import copy

#
# #shallow copy
#
# mylist1 = [1,2,3,4,5]
# mylist2 = mylist1
# mylist2[3]= 20
#
# print(mylist1)
# print(mylist2)



# mylist1 = [1,2,3,4,5]
# mylist2 = mylist1.copy()
# mylist2[3]= 20
#
# print(mylist1)
# print(mylist2)

mylist1 = [1,2,3,[1,2,3,4],5]
mylist2 = copy.copy(mylist1)
mylist2[1]=112
mylist2[3][2]= 20


print(mylist1)
print(mylist2)

mylist1 = [1,2,3,[1,2,3,4],5]
mylist2 = copy.deepcopy(mylist1)
mylist2[1]=112
mylist2[3][2]= 20

print(mylist1)
print(mylist2)