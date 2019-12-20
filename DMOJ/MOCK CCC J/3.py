t = int(input())
for i in range(t):
    ai,bi,ni = input().split()
    ai = int(ai)
    bi = int(bi)
    ni = int(ni)
    temp = 0
    while True:
        temp += ai
        if temp > ni:
            print ("NO")
            break
        if ((ni - temp) % ai ==0) or ((ni - temp) % bi ==0) or (ni % temp == 0):
            print("YES")
            break
        temp += bi
        if temp > ni:
            print("NO")
            break
        if ((ni - temp) % ai ==0) or ((ni - temp) % bi ==0) or (ni % temp == 0):
            print("YES")
            break
    
