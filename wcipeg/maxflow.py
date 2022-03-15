#MaxFlow
t=int(input())
for i in range(t):
    n=int(input())
    maxnum=0
    for a in range(n):
        f=int(input())
        if f>maxnum:
            maxnum=f
    print(maxnum)
