# #string
# try:
#     myname = "sandeep"
#     print(myname)
#     myname[2]='d'
# except TypeError:
#     print("exception occured")
#     print(type(myname))
#
# try:
#     mylist = [1,2,3,4]
#     print(mylist)
#     print(mylist[4])
#     print(type(mylist))
# except IndexError:
#     print("Index out of range")
#     print(type(mylist))
#
# try:
#     mytuple = (1,2,4,2,3)
#     print(mytuple)
#     mytuple[3] = 22
#     print(mytuple[10])
# except (ValueError,IndexError,TypeError):
#     print("error")

mystring = "sandeep is from hyd"
print(mystring[-1])
# print(mystring[-21])
print(mystring[2:5])

# #print i didn't get any information
#
# mystring = 'i didn\'t get any information '
#
# print(mystring)

#String formatting

#1)defaault formatting

print("{} is from {}".format("sandeep","hyd"))
#positional formatting
print("{1} is from {0}".format("hyd","sandeep"))
#keyword formatting
print("{name} is from {location}".format(location = "hyd",name = "sandeep"))
