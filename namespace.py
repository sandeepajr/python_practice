var =10
def outer_func():
    global var
    var = var+10
    print("var value is {}".format(var))
    print(f"var value is {var}")
    def internal():
        var1 =20
        print(f"var1 is {var1}")
outer_func()
print(var)
print(var1)