text = input()
vertical = 0
horizontal = 0
for char in text:
    if char == "V":
        vertical += 1
    if char == "H":
        horizontal += 1

nH = horizontal%2
nV = vertical%2

if nH == 0 and nV == 0:
    print(1,2)
    print(3,4)
if nH == 0 and nV == 1:
    print(2,1)
    print(4,3)
if nH == 1 and nV == 0:
    print(3,4)
    print(1,2)
if nH == 1 and nV == 1:
    print(4,3)
    print(2,1)
