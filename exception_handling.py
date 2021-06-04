# '''this is to practice exception handling'''
#
# try:
#     # a=10
#     # b=20
#     # print("a divided by b-b is {}".format(a/(b-b)))
#     mylist = [1,2,3,4]
#     print(mylist[4])
# except (IndexError,IndentationError):
#     print("execept block")
# except ZeroDivisionError:
#     print("not dividable")

# #--------------------------------------------------
# try:
#     a = int(input("enter number"))
#     b=10
#     print(b/a)
# except ValueError:
#     print("cant be converted to integer")
# except ZeroDivisionError:
#     print("cant be divided by 0")
# else:
#     print(b/a)
# finally:
#     print("ececution done")
# #--------------------------------------------------

#try raise
#-------------------------------------------------

# try:
#     raise NameError("hiii")
# except NameError as errorname:
#     print("name errror occured")
#     print(errorname)
#     # raise
#-------------------------------------------------

# a=12
# try:
#     assert a == 10
# except AssertionError:
#     print("not equal and test failed")
#-------------------------------------------------



