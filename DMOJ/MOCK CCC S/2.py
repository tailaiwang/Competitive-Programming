n = int(input())
bigBox = []
for i in range (n):
    temp = []
    temp = input().split()
    bigBox.append(temp)
total = 0
for y in range (n):
    flag = False
    for x in range (n):
        if (x < n - 1 and int(bigBox[y][x]) != int(bigBox[y][x+1]) - 1 and flag == False):
            flag = True
            total += 1
print(total)
        
