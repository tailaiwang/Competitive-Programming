n = int(input())
l = []
total = 0
for i in range (n):
    temp = int(input())
    l.append(temp)
for num in l:
    total += num
print (round(total/len(l), 1))
