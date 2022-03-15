#Mode
numList=[]
occurences=[]
outList=[]
while True:
    a=int(input())
    if a!=-1:
        numList.append(a)
    else:
        break
for i in numList:
    mode=numList.count(i)
    occurences.append(mode)
b=max(occurences)
for i in range(len(occurences)):
    if occurences[i]==b and numList[i] not in outList:
        outList.append(numList[i])
outList.sort()
for i in outList:
    print(i)
