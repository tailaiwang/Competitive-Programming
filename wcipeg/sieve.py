#sieve
n=int(input())
list1=[]
for i in range(1,n+1):
    list1.append(i)
    count=0
    for x in list1:
        if i%x==0:
            count+=1
            if count>2:
                count=0
                print(0)
                break
            if i==x and count<3:
                if i==1:
                    print(0)
                elif i==2 or i==3:
                    print(1)
                else:
                    print(1)
        
