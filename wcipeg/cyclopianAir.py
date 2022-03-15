#CyclopianAir
cards=[]
maxValue=0
n=int(input())
for i in range(n):
    a=int(input())
    cards.append(a)
for i in range(len(cards)-1):
    if cards[i]*cards[i+1]>maxValue:
        maxValue=cards[i]*cards[i+1]
if cards[-1]*cards[0]>maxValue:
    maxValue=cards[-1]*cards[0]
print(maxValue)
    
