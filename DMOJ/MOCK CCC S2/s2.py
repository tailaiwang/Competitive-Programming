x,y,x1,y1,x2,y2 = input().split()

x = int(x)
y = int(y)
x1 = int(x)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)


if x1 <= x <= x2 or x2 <= x <= x1:
    if (abs(x1 - x) > abs(x2 - x)):
        print(round((x2-x),3))
    else:
        print(round((x1-x),3))

elif y1 <= y <= y2 or y2 <= y <= y1:
        if(abs(y1 - y) > abs(y2 - y)):
           print(round((y2 - y),3))
        else:
           print(round((y1 - y),3))
