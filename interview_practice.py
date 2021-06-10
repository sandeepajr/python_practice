L1 = [1,2,[],[],3,4,[],[1,2]]
L2 = []

for item in L1:
    if item:
        L2.append(item)
        print(item)
print(L2)

L3 = [item for item in L1 if not item]
print(L3)