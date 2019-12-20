#EngOrFr
n=int(input())
lines=""
for i in range(n):
    line=input()
    line=line.lower()
    lines+=line
countS=lines.count("s")
countT=lines.count("t")
if countS>countT or countS==countT:
    print("French")
else:
    print("English")
    
