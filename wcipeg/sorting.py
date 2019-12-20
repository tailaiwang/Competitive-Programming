#sorting
list1=[]
out=[]
n=int(input())
for i in range(n):
    c=int(input())
    list1.append(c)
for i in range(len(list1)):
    out1=min(list1)
    list1.remove(out1)
    out.append(out1)
for i in out:
    print(i)
    
