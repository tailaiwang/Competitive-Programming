n,x  = input().split(" ")
m = input().split(" ")
totalQuality = 0
for i in range(int(x)):
    totalQuality += int(max(m))
    for i in m:
        if i == max(m):
            i = int(i) - 1
print(totalQuality - 1)

        
