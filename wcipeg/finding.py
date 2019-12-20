#find the character
let=input()
string=input()
temp=string.lower()
count=0
for letter in temp:
    if letter==let:
        count+=1
print(string)
print(count)
