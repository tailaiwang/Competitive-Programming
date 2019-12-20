#up&down
nikky=0
byron=0
a=int(input())
b=int(input())
c=int(input())
d=int(input())
s=int(input())
for i in range(1,s+1):
    if i%2!=0:
        nikky+=a
        byron+=c
    else:
        nikky-=b
        byron-=d
if byron>nikky:
    print("Byron")
elif nikky>byron:
    print("Nikky")
elif nikky==byron:
    print("Tied")
        
        
