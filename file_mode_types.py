# file_read_obj = open("sandeep2.txt",'r')
# print(file_read_obj.read())
# file_read_obj = open("sandeep2.txt",'r+')
# print(file_read_obj.read())
# file_read_obj.write("newline")
# print("----------------------------")
# file_read_obj.close()
# file_read_obj = open("sandeep2.txt",'r+')
# # print(file_read_obj.read())
# mylist = ["sandeep\n", "is\n", "from\n","hyd\n"]
# file_read_obj.writelines(mylist)

#practice for read, readline, readlines
#
# file_read_obj = open("sandeep2.txt",'r+')
# # # print(file_read_obj.read())
# # for each_line in file_read_obj:
# #     print(each_line)
# #     print("---------------")
# #     print(file_read_obj.readline())
# print(file_read_obj.readlines())

file_content = '''this is line no1
this is line no2
this is line no3
this is line no4
this is line no5'''

# file_write = open("sandeep2.txt",'w+')
# file_write.write(file_content)
# file_write.seek(0)
# print(file_write.readline())
# file_write.write("\n new line")
# print(file_write.readline())
# file_write.close()

file_write = open("sandeep2.txt",'r+')
file_write.write(file_content)
# file_write.seek(0)
# print(file_write.readline())
# print(file_write.tell())
# file_write.write("\n new line")
# print(file_write.readline())
# print(file_write.fileno())
# print(file_write.isatty())
file_write.close()

# file_read_plus = open("sandeep2.txt",'r+')
# file_read_plus.write("sandeep")
# file_read_plus.seek(0)
# print(file_read_plus.read())
# file_read_plus.seek(10)
# print(file_read_plus.readline())
# file_read_plus.seek(0)
# print(file_read_plus.readlines())
# file_read_plus.close()

# file_write_plus = open("sandeep2.txt",'w+')
# file_write_plus.write("sandeep")
# file_write_plus.close()
#
#file.next example

file_read_write = open("sandeep2.txt","r+")
try:
    while True:
        line = next(file_read_write)
        if line == "":
            break
        print(line)
except StopIteration:
    pass


# # #read complete content using readline
#
# file_read_write = open("sandeep2.txt",'r+')
# myline = file_read_write.readline()
# while myline:
#     print(myline)
#     myline=file_read_write.readline()
# file_read_write.close()