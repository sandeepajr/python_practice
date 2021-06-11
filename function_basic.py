# #define a function and call
# def output_enterednum():
#
#     '''This function is to print the entered number'''
#     num = input("enter number")
#     print("entered number is {}".format(num))
# output_enterednum()
# print(output_enterednum.__doc__)
# help(output_enterednum)
#
# def output_addnumbs(a,b):
#     addnum = a+b
#     print("sum is {}".format(addnum))
# a = 10
# b = 20
# output_addnumbs(a,b)


def my_func_to_printname():
    '''This functions is to print name without arguments'''
    print("my name is sandeep")
print(my_func_to_printname.__doc__)
my_func_to_printname()

def my_func_with_arg(name):
    '''--------------------------
This functions is to print name with arguments
------------------------------------------------'''

    print(f"my name is {name}")
print(my_func_with_arg.__doc__)
my_func_with_arg("rani")
