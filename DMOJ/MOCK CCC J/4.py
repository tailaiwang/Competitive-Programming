n = int(input())
l = [0,0,0,0]
for i in range(n):
    temp = input()
    if temp == "Deluxe Tuna Bitz":
        l[0] += 1
    elif temp == "Bonito Bitz":
        l[1] += 1
    elif temp == "Sashimi":
        l[2] += 1
    elif temp == "Ritzy Bitz":
        l[3] += 1      
l2 = [0,0,0,0]
l2[0] = l[0]
l2[1] = l[1]
l2[2] = l[2]
l2[3] = l[3]

flag1 = True
flag2 = True
flag3 = True
flag4 = True
l.sort(reverse = True)
for item in l:
    count = 0
    while count < 4:
        if item == l2[count]:
            if count == 0 and item != 0 and flag1:
                print("Deluxe Tuna Bitz " + str(item))
                flag1 = False
                break
            elif count == 1 and item != 0 and flag2:
                print("Bonito Bitz " + str(item))
                flag2 = False
                break
            elif count == 2 and item != 0 and flag3:
                print("Sashimi " + str(item))
                flag3 = False
                break
            elif count == 3 and item != 0 and flag4:
                print("Ritzy Bitz " + str(item))
                flag4 = False
                break
        count += 1
