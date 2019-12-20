#3nplus1
b=int(input())
count=0
def collatz(b):
    l=[b]
    if b==1:
        return 1
    elif b%2==0:
        l.append(collatz(b/2))
    else:
        l.append(collatz(b*3+1))
    return l
print(len(l))
collatz(7)
        
    
    
    
