#python lists (easy)
temp = []
n = int(input())
for i in range(n):
    instruction = input().split(" ")
    if instruction[0] == 'insert':
        temp.insert(int(instruction[1]), int(instruction[2]))
    elif instruction[0] == 'print':
        print(temp)
    elif instruction[0] == 'remove':
        temp.remove(int(instruction[1]))
    elif instruction[0] == 'append':
        temp.append(int(instruction[1]))
    elif instruction[0] == 'sort':
        temp.sort()
    elif instruction[0] == 'pop':
        temp.pop()
    elif instruction[0] == 'reverse':
        temp.reverse()
    else:
        print('error')
    
