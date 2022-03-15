#pandemonium
diffs=[]
n=int(input())
d=input().split()
for a in d:
    if a not in diffs:
        diffs.append(a)
print(len(diffs))
    
