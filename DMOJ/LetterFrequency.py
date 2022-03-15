s = input()
q = int(input())
for i in range (q):
    count = 0
    temp = input().split(" ")
    for x in range (int(temp[0]), int(temp[1])):
        if s[x] == temp[2]:
            count += 1
    print (count)
            
