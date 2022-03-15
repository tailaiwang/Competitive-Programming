s = input()
t = input()
k = int(input())
count = 0
count2 = 0
condition = False
for char in t:
    if char != s[count2]:
        count += 1
        if char != " " and s[count2] == " ":
            condition  = True
        elif char == " " and s[count2] != " ":
            condition = True
    count2 += 1

if (count <= k and condition == False):
    print("Plagiarized")
else :
    print("No plagiarism")
