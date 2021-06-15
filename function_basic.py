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
###############################################################
def my_fun_withoutarg_practice():
    def my_func_to_printname():
        '''This functions is to print name without arguments'''
        print("my name is sandeep")
    print(my_func_to_printname.__doc__)
    my_func_to_printname()

###############################################################
def my_fun_witharg_practice():
    def my_func_with_arg(name):
        '''--------------------------
    This functions is to print name with arguments
    ------------------------------------------------'''

        print(f"my name is {name}")
    print(my_func_with_arg.__doc__)
    return_value = my_func_with_arg("rani")
    print(return_value)
    assert return_value == None


##############################################################################

def myfun_pass_by_reference():
    '''validate pass by reference'''
    def pass_by_reference(mylist):
        '''pass by reference validation'''
        mylist[0] = 0

    mylist = [1,2,3,4]
    pass_by_reference(mylist)
    print(mylist)
    #
    # def pass_by_referenceint(myint):
    #     '''pass by reference validationint'''
    #     myint = 0
    #
    # myint = 1009
    # pass_by_referenceint(myint)
    # print(myint)
##############################################################################
def myfun_pass_by_value():
    '''validate pass by value'''
    def pass_by_value(mylist):
        mylist = [11,22,33,44]
    mylist = [1,2,3,4]
    pass_by_value(mylist)
    print(mylist)
##############################################################################

def defaultargs_validation():
    def default_arg (x,y=10):
        print(f"value passed are {x} and {y}")
    default_arg(2)
    default_arg(3,5)
    #
    # def default_arg_wrongorder (x=10,y):
    #     print(f"wrong order value passed are {x} and {y}")
    # default_arg_wrongorder(x=2)

##############################################################################

def keywordargs_validation():
    def default_arg (x,y=10):
        print(f"value passed are {x} and {y}")
    default_arg(10,y=2)
    default_arg(y=3,x=5)
##############################################################################
def variable_len_nonkeywordvalidation():
    def add_all_args(*arguments):
        '''variable length no keyword'''
        sum = 0
        for item in arguments:
            sum+= item
        print(sum)
    add_all_args(1,2,4,3)
    def add_all_args(arg1,*arguments):
        '''variable length no keyword'''
        sum = 0
        for item in arguments:
            sum+= item
        print(sum)
    add_all_args(1,2,4,3)
##############################################################################
def variable_len_keywordvalidation():
    '''keyword variable args'''
    def kw_variable_args_validation(**arguments):
        for key,value in arguments.items():
            print (f"key is {key}, value is {value}" )
    kw_variable_args_validation(name="sandeep",surname="adapa" )
##############################################################################
def lamda_validation():
    square = lambda x:x*x
    print(square(2))
    print(square(3))



# my_fun_withoutarg_practice()
# my_fun_witharg_practice()
# myfun_pass_by_reference()
# myfun_pass_by_value()
# defaultargs_validation()
# keywordargs_validation()
# variable_len_nonkeywordvalidation()
# variable_len_keywordvalidation()
lamda_validation()