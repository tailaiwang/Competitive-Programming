#RemoveCancer
x=int(input())
for i in range(x):
    line=input()
    for char in line:
        if char!="1" or char!="0":
            line.replace(char,"0")
            print(line)
