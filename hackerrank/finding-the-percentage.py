#finding-the-percentage
n = int(input())
def find_percentage(n):
    outputlist = []
    for i in range (0,n+1):
        temp = input().split(" ")
        if len(temp) == 1:
            for item in outputlist:
                if item[0] == temp[0]:
                    return(item[1])
        runningsum = 0
        for i in range(1,len(temp)):
            runningsum += int(temp[i])
        outputlist.append([temp[0], runningsum/(len(temp)-1)])
print(find_percentage(n))
    
    
