#Multiple Choice
n = int(input())
answered = ""
count = 0
correct = 0
for i in range(n):
    answered += input()
for i in range (n):
    temp = input()
    if temp == answered[count]:
        correct += 1
    count += 1
print(correct)
