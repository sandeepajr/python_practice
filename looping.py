#program for learning looping
mylist = ["apple","orange","watermelon","muskmelon",12,12.5]

for item in mylist[1:3]:
    print(item)

for item in mylist:
    print(type(item))
    if(type(item).__name__ == "str"):
        print(item,end=" ")
print(True+True)

for item in mylist:
    # print(type(item))
    if(type(item) is str):
        print(item,end=" ")
print(True+True)