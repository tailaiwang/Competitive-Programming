#first primes
T = int(input())
for i in range(T):
    n = int(input())
    primes = [2,3]
    for y in range (1,2*n,2):
        flag = True
        for x in range (2,int(y**0.5) + 1):
            if y % x == 0:
                flag = False
            if x == int(y ** 0.5) and flag:
                primes.append(y)
    bigFlag = True
    for num in primes:
        for num2 in primes:
            if (num + num2)/2 == n and bigFlag:
                print(num,num2)
                bigFlag = False
        

