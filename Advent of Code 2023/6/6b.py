'''

So, the example from before:

Time:      7  15   30
Distance:  9  40  200
...now instead means this:

Time:      71530
Distance:  940200
Now, you have to figure out how many ways there are to win this single race. In this example, the race lasts for 71530 milliseconds and the record distance you need to beat is 940200 millimeters. You could hold the button anywhere from 14 to 71516 milliseconds and beat the record, a total of 71503 ways!

How many ways can you beat the record in this one much longer race?
'''

file = open("input.txt", "r").read()
lines = file.split("\n")
times = lines[0].split(": ")[1].split()
distances = lines[1].split(": ")[1].split()

total_time = ""
for time in times:
    total_time += time

total_distance = ""
for distance in distances:
    total_distance += distance

time = int(total_time)
record = int(total_distance)
lhs = 0
rhs = time - 1
while True:
    distance = lhs * (time - lhs)
    if distance > record:
        break
    lhs += 1

# rhs
while True:
    distance = rhs * (time - rhs)
    if distance > record:
        break
    rhs -= 1
print(rhs - lhs + 1)
