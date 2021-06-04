a1 = 10
b1 = 10
print("id of a1 is {}, id of b1 is {}".format(id(a1),id(b1)))
if a1 is b1:
    print("same id")
else:
    print("different")

a1 = "sandeep"
b1 = "sandeep"
print("id of a1 is {}, id of b1 is {}".format(id(a1),id(b1)))
if a1 is b1:
    print("same id")
else:
    print("different")

a1 = [1,2,3]
b1 = [1,2,3]
print("id of a1 is {}, id of b1 is {}".format(id(a1),id(b1)))
if a1 is b1:
    print("same id")
else:
    print("different")

if a1 == b1:
    print("same value")
else:
    print("different")