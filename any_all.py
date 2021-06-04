my_truelist = [True,True,True]
my_falselist = [False,False,False]
myboth = [True,False,False]
empty = []
print(any(my_falselist))
print(any(my_truelist))
print(any(myboth))

print(all(my_falselist))
print(all(my_truelist))
print(all(myboth))
print(any(empty))
print(all(empty))


x = 5
print(type(x))
if (type(x) is int):
    print("true")
else:
    print("false")