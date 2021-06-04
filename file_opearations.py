# #file operation practice
#
# file_obj = open("sandeep.txt","r")
# print(file_obj.read(10))
# # file_obj = open("sandeep.txt","r")
# for eachline in file_obj:
#     print(eachline.lstrip(),end='')
#
# file_obj_write = open("sandeep2.txt","w")
# file_obj_write.write("sandeep \n ")
# mylist = [1,2,4,4,5,]
# file_obj_write.write(str(mylist))
file_obj_append = open("sandeep.txt","a")
file_obj_append.write("\nappeinf this line")
file_obj_append.close()

with open("sandeep.txt",'r') as file_obj:
    for eachline in file_obj:
        print(eachline)
        words = eachline.split()
        print(words)
file_obj_append = open("sandeep_rplus.txt","r+")

