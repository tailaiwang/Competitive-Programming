#similies
nouns=[]
adjs=[]
n=int(input())
m=int(input())
for i in range(n):
    adj=input()
    adjs.append(adj)
for i in range(m):
    noun=input()
    nouns.append(noun)
for i in adjs:
    for x in nouns:
        print(i,"as",x)
