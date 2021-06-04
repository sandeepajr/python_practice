#program is to test while loop

mylist = [x for x in input("enter values").split()]
rev_list = []
length = len(mylist)
print(length)
while (length>0):
    print(mylist[length-1])
    rev_list.append(mylist[length-1])
    length-=1
print(rev_list)