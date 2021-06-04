'''Training fro fresshers, day1 exercise
input,output arguments'''

# # 1) Ready two integers from user input seperated by ',' and print the sum
# x,y = input("enter two numbers seperated by ','").split(',')
# print(f"entered values are 1st is {x} 2nd is {y}")
# print(int(x)+int(y))

#  #2)Ready multiple inputs from user input seperated by ',' to a List and print List
# input_list = [x for x in input("Enter values").split(',')]
# print(input_list)

# '''3)Ready name and location form user input and print in below format
# eg:  input ram, hyderabad
#  o/p : entered name is Ram and location is hyderabad'''
#
# name,location = input("Enter name and location").split(',')
# print(f"Entered name is {name} and location is {location}")
# print("Entered name is {} and location is {}".format(name,location))
# print("Entered name is {1} and location is {0}".format(location,name))


# '''4)Print multiple string using single print with '$' inbetween
# eg: "Hi" "hello" "Wold"
# o/p: Hi $ hello $ World'''
#
# print("hi","hello","world",sep=' $ ')

# '''5)miltiple print statements o/p in single line
# eg: print("hi")
# print ("hello")6)
# print("World")
# o/p: hi Hello World'''
#
# print("hi",end=" ")
# print("hello",end=" ")
# print("world",end=" ")

# '''6)Print output center alligned with lenght 6
# eg: if user try to print srtings of diff lenght  "hi""hello""World"
# o/p:
#    hi
#  hello
#  World'''
# my_str = "hi"
# my_str2 = "hello"
# my_str3 = "worlds"
# print(my_str.center(20,' '))
# print(my_str2.center(20,"*"))
# print(my_str3.center(20,"*"))
# print(my_str.ljust(20,'*'))
# print(my_str2.center(20,"*"))
# print(my_str3.rjust(20,"*"))

#Operators practice

# #1)Take two values from user and perform arthematic operations(add, sub, multi, division, division to floor, modulus,power) on inputs received
#
# x,y = input("enter 2 iteger values").split(',')
# x = int(x)
# y = int(y)
# # print(type(x),type(y))
# print("sum is {}".format(x+y))
# print("sub is {}".format(x-y))
# print("mul is {}".format(x*y))
# print("div is {}".format(x/y))
# print("Modulus is {}".format(x%y))
# print("divofloor is {}".format(x//y))
# print("power is {}".format(x**y))

# #2)Take two values from user and perform relational operations(>,<,==,!=,<=,>=) on inputs received
# my_list = [int(x) for x in input("enter 2 integer values").split(',')]
# x,y = my_list
# # print(type(x),type(y), sep='***')
# print(x>y)
# print(x<y)
# print(x==y)
# print(x<=y)
# print(x>=y)
# print(x!=y)

# # #3)Logic'al operator. Take two variables True and False, perform logical operations (And, Or,not)
# my_true = True
# my_False = False
#
# print(my_true and my_False)
# print(my_true and my_true)
# print(my_true or my_False)
# print(not my_true)
# print(not my_False)

#4)identity operator:  take two integers and two lists and copmpare identity. Print output

x,y = 2,2
mylist1 = [1,2,3,4]

mylist2 = [1,2,3,4]
mystring1 = "sandeep"
mystring2 = "sandeep"
print(id(mylist1))
print(id(mylist2))
print(mystring1 is mylist2)
print(id(x))
print(id(y))
print(id(mylist1))
print(id(mylist2))
print(x is y)
print(mylist1 is mylist2)

# '''6)Membership: Validate is a letter or substring is in the parent string or item in list
# eg: "sandeep" if a letter is in string print true else false'''
#
# mystring = input("enter string").split()
# substring = 'z'
# substring2 = 'e'
# print(substring in mystring)
# print(substring2 in mystring)
#
#
# # my_list = [1,2,3,4,5]
# # my_search_item = 5
# # print(my_search_item in my_list)
# # my_list = ['a','b','g','e','d']
# # my_search_item = 'a'
# # print(my_search_item in my_list)
#
# mystring = "sandeep"
# substring = 'zd'
# substring2 = 'eep'
# print(substring in mystring)
# print(substring2 in mystring)

# #7 Ternary operator Print min value of two input values in single line
# a = 100
# b = 20
# print(a if a<b else b)

# #8 Take two lists and print overlapping items
# my_list1 = [1,2,3,4,5,6,7,8]
# my_list2 = [2,3,11,43,4,2]
# for item in my_list2:
#     if item in my_list1:
#         print(item,end=">>>")


    # input1 = input("Enter numbers to a list separated by ',' : ").split(",")
    # input1 = [int(i) for i in input1]
    # print(input1)
    # input2 = input("Enter numbers to a list separated by ',' : ").split(",")
    # input2 = [int(i) for i in input2]
    # print(input2)
    # input1 = [1,2,4,5]
    # input2 = [2,3,4]
    #
    # print(list(set(input1) & set(input2)))