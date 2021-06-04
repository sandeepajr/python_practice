# mylist = [int(x) for x in input("entervalue").split()]
# for item in mylist:
#     print(item)

for item in range(20,10,-2):
    print(item)

for item in range(10,20,2):
    print(item)

for letter in "sandeep":
    if letter == "e":
        continue
    print(letter,end='')

for letter in "sandeep":
    if letter == "e":
        break
    print(letter,end='')