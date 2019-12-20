n =int(input())
for i in range(n):
    a,b,c = input().split()
    
    if (int(a) * int(b) == int(c)):
        print("POSSIBLE DOUBLE SIGMA")
    else:
        print("16 BIT S/W ONLY")
