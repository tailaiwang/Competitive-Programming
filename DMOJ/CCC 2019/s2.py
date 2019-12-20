primes =[]
check = [2]
count = 0
for i in range(3,2000000):
    check.append(i)
    for x in check:
        flag = True
        if i == x and len(check)>1:
            primes.append(i)
            count += 1
            print(count)
            flag = False
        if i % x == 0:
            break
print(primes)
