#shuffle
original=["A","B","C","D","E"]
out=""
while True:
    b=int(input())
    n=int(input())
    if b==1:
        for i in range(n):
            temp=original[0]
            del original[0]
            original.append(temp)
    if b==2:
        for i in range(n):
            temp=original.pop()
            original.insert(0,temp)
    if b==3:
        for i in range(n):
            temp=original[0]
            del original[0]
            original.insert(1,temp)
    if b==4 and n==1:
        for i in original:
            out+=(i+" ")
        print(out)
        break
        
        
