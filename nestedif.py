'''practice
nested if
'''

i = 2

if i>5:
    print("is is larger than 5")
    if i>7:
        print("greater than 7 also")
    if i==10:
        print("i is 10")
    else:
        print("not10")
#short hand if

if i>5: print("i greater than 5")

#short hand elsif
print("greater than 5") if i>5 else print("less than 5")