#middle
one=int(input())
two=int(input())
three=int(input())
num=[]
num.append(one)
num.append(two)
num.append(three)
num.remove(max(num))
num.remove(min(num))
print(num[0])
