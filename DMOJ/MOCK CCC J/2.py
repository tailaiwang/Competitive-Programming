count = 0
output = 0
correct = "pusheen"
s = input()
for char in s:
    if char != correct[count]:
        output += 1
    count += 1

print(output)
