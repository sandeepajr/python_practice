import string

mystring = "    this is sandeep from amp working in innominds. sandeep is working on python   "
name ="sandeep"

print(string.ascii_letters)
print(string.ascii_lowercase)
print(mystring.startswith("this") and mystring.endswith("indts"))

print(mystring.index("sandeep"))
# print(mystring.index("ram"))
print(name.isalpha())
print(name.upper())
print(name)
print(name.swapcase())
print(mystring.replace("sandeep","ram"))
print(mystring.count("sandeep"))

print(mystring.index("sandeep"))
print(mystring.find("sandeeps"))
mylist = ["sandeep","rani","Shanvith"]
sep = '$'
print(sep.join(mylist))
print(mystring.lstrip(''))
print(max(mystring))
print(min(mystring))
print(mystring.split())


