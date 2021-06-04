
import time,io
print("entername",end="$$")
print("entername")

for x in reversed(range(4)):
    print(x,"ready",end=">>>",flush=True,sep="$")
    time.sleep(1)

dummy_file = io.StringIO
print("sandeep",file=dummy_file)
print("content", dummy_file.getvalue())