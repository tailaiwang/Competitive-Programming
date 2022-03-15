#fire
smallest=[]
otherSmall=[]
n,k=input().split()
leaves=input().split()
for i in range(int(k)):
    smallest.append(min(leaves))
    leaves.remove(min(leaves))
for i in leaves:
    for x in smallest:
        if i<x*2:
            otherSmall.append(i)
if len(otherSmall)!=0:
    print(min(otherSmall))
elif len(leaves)>0:
    print(min(leaves))
else:
    print(int(min(smallest))*2)


