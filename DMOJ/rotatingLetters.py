word = input()
output = "YES"
valid = "IOSHZXN"
for char in word:
    if char not in valid:
        output = "NO"
print(output)
