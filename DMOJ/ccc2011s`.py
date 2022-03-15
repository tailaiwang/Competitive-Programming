#CCC11 S1
n = int(input())
s = 0
t = 0
for i in range(n):
    temp = input()
    for char in temp:
        if char == "t" or char == "T":
            t += 1
        elif char == "s" or char == "s":
            s += 1
if t > s:
    print("English")
else:
    print("French")
