'''
For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.
'''

file = open("input.txt", "r")
counter = 1
limit = {"red": 12, "green": 13, "blue": 14}
sum = 0
for line in file.readlines():
    line = line.strip("\n")
    line = line.split(": ")
    draws = line[1]
    draws = draws.split("; ")
    flag = False
    for draw in draws:
        balls = draw.split(", ")
        for ball in balls:
            color = ball.split(" ")[1]
            number = ball.split(" ")[0]
            if limit[color] < int(number):
                flag = True
                break
        if (flag):
            break
    if not flag:
        sum += counter
    counter += 1
print(sum)


    