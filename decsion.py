#program is to practice decsion statements

# a,b,c = input("enter values with seperator as ,").split()
# print ("entered values are",a,b,c,sep="__")

# mylist = input("enter values with seperator as ,").split(',')
mylist = [int(x) for x in input("entervalues").split()]
print(mylist)
min = mylist[0]
for item in mylist:
    if item > min:
        continue
    else:
        min = item
print(min)

print(mylist.sort())
print(mylist)