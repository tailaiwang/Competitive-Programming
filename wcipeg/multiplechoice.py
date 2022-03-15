#multiplechoice
n=int(input())
students=[]
teachers=[]
count=0
for a in range(n):
    student=input()
    students.append(student)
for b in range(n):
    teacher=input()
    teachers.append(teacher)
for i in range(n):
    if students[i]==teachers[i]:
        count+=1
print(count)
        
    
    
