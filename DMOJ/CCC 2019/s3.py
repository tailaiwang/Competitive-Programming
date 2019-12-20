#s3
l1 = input().split()
l2 = input().split()
l3 = input().split()

x1 = []
x2 = []
x3 = []
for i in range(0,3):
    if l1[i] == "X":
        x1.append(i)
    else:
        l1[i] = int(l1[i])
    if l2[i] == "X":
        x2.append(i)
    else:
        l2[i] = int(l2[i])
    if l3[i] == "X":
        x3.append(i)
    else:
        l3[i] = int(l3[i])
for char in x1:
    if len(x1) == 1:
        if char == 0:
            l1[0] = l1[1] - (l1[2] - l1[1])
        if char == 1:
            l1[1] = int((l1[2]+l1[0])/2)
        if char == 2:
            l1[2] = (l1[1] + (l1[1] - l1[0]))
for char in x2:
    if len(x2) == 1:
        if char == 0:
            l2[0] = l2[1] - (l2[2] - l2[1])
        if char == 1:
            l2[1] = int((l2[2]+l2[0])/2)
        if char == 2:
            l2[2] = (l2[1] + (l2[1] - l2[0]))
for char in x3:
    if len(x3) == 1:
        if char == 0:
            l3[0] = l3[1] - (l3[2] - l3[1])
        if char == 1:
            l3[1] = int((l3[2]+l3[0])/2)
        if char == 2:
            l3[2] = (l3[1] + (l3[1] - l3[0]))

print(l1)
print(l2)
print(l3)






