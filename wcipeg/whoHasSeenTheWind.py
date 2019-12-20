#whoHasSeenTheWind
h=int(input())
m=int(input())
q=False
for i in range(1,m):
    if -6*i**4+h*i**3+2*i**2+i<=0:
        print("The ballon first touches the ground at hour: \n",i)
        q=True
        break
if q==False:
    print("The balloon does not touch ground in the given time.")
