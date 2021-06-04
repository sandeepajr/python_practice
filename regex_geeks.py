import re
new_split = re.split("\s","Words, words ,Words")
print(new_split)

new_split = re.split("\W+","Words, words ,Words")
print(new_split)

print(re.split('\W+', 'On 12th Jan 2016, at 11:02 AM'))

print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM'))

print(re.split('[a-f]+', 'Aey, Boy oh boy, come here', flags = re.IGNORECASE))

# Lets use a regular expression to match a date string
# in the form of Month name followed by day number
regex = r"([a-zA-Z]+) (\d+)"
regex = r"[a-z]+ \d+"
match = re.findall(regex, "I was born on June 24",flags= re.IGNORECASE)
# print(match.start())
print(match)


express = re.compile("a...s$")
matched = express.search("this is an a123s")
print(matched)
print(matched.start())


express = re.compile("[abd]")
matched = express.search("this ddis aan a123s")
print(matched)
print(matched.start())

input = input("enter value")
match = re.search("[\+|\-]*\d*\.+\d",input)

if(match):
    print("its floating number")
else:
    print("non floating number")