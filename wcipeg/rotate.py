word=input()
rotate= "IOSHZXN"
answer= "YES"
for letter in word:
    if letter not in rotate:
        answer= "NO"
print (answer)
    
