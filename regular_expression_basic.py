import re
my_string = '''sandp this is sandeep from hyd, my pin is 500089, dob is 23-10-1985 sandp'''
#findall withh return list of pattern matching
print(re.findall(r'.+',my_string))

print(re.findall('.+',my_string))

regular = re.compile('[a-e0-8]+')
print(regular.findall(my_string))
print(re.search('[a-e]+',my_string))

import re
txt = "this is -snadeep  - from hyd, my pin is 500089, dob is 23-10-1985"
#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]+", txt)
x = re.findall("\d+", txt)
x = re.findall("\D+", txt)
x = re.findall("-\d+", txt)
x = re.findall("\w+", txt)
print(x)
x = re.findall("\W+", txt)
print(x)
x = re.findall("-\w+", txt)
print(x)
x = re.findall("\s+", txt)
print(x)
x = re.findall("\S+", txt)
print(x)
x = re.findall("-\s+", txt)
print(x)


my_regex = re.compile("\D+")
print(my_regex.findall(my_string))


my_regex = re.compile("ab+")
print(my_regex.findall("ababbababaaabbbb"))

print("-------------------------------")
myregex = re.compile("sand(.+?)p")
print(myregex.findall(my_string))

myregex = re.compile("sand.+")
print(myregex.findall(my_string))


myregex = re.compile("sand*")
print(myregex.findall(my_string))

myregex = re.compile("sande{2}p")
print(myregex.findall(my_string))

myregex = re.compile("sand.{2}")
print(myregex.findall(my_string))

my_string2 = "Hello world"
myrgx = re.compile("rld$")
print(myrgx.findall(my_string2))


myregex = re.compile("[andeep]")
print(myregex.findall(my_string))

myregex = re.compile("[a-n]")
print(myregex.findall(my_string))

#not the selected characters
myregex = re.compile("[^andeep]")
print(myregex.findall(my_string))

txt = "8 times before 11:45 AM"

#Check if the string has any two-digit numbers, from 00 to 59:

x = re.findall("[0-5][0-9]", txt)
print(x)

#no spl meaning but simple :

txt = "8 times before 11:45 AM"

#Check if the string has any + characters:

x = re.findall("[:]", txt)




txt = "The rain in Spain"
# x = re.search("in", txt)
# print(x)
#
# print("The first white-space character is located in position:", x.start())

txt = "The rain in Spain"
x= re.split("\s",txt)
print(x)

x= re.split("\s",txt,1)
print(x)

x= re.compile('in')
op = x.sub("on",txt)
print(op)
op = re.sub('in','on',txt,1)
print(op)

