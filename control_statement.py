mylist = ["apple",'watermelon',22,55,23,"sandep"]
fruits = []
for item in mylist:
    print(type(item))
    if type(item) is str:
        fruits.append(item)
        continue
    if type(item) is int:
        pass
    print(item)
print(fruits)