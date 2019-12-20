#dpa
a=int(input())
for x in range(a):
    n=int(input())
    count=0
    for i in range(1,n-1):
        if n%i==0:
            count+=i
    if count==n:
        print(n,"is a perfect number.")
    if count<n:
        print(n,"is a deficient number.")
    if count>n:
        print(n,"is an abundant number.")
