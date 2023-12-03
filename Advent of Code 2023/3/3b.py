'''
Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?
'''

digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
gears = {}

def grid_check(grid, x, y):
    return True if x <= len(grid) - 1 and x >= 0 and y <= len(grid[0]) - 1 and y >= 0 else False

def helper(grid, i, j):
    valid = False
    gear_x = 0
    gear_y = 0
    total = ""
    while (grid_check(grid, i, j) and grid[i][j] in digits):
        for direction in directions:
            x = i + direction[0]
            y = j + direction[1]
            if grid_check(grid, x, y):
                if grid[x][y] not in digits and grid[x][y] == "*":
                    gear_x = x
                    gear_y = y
                    valid = True
        total += grid[i][j]
        j += 1
    print(total, valid)
    if valid:
        if (gear_x, gear_y) in gears:
            return(j, int(total) * gears[(gear_x, gear_y)])
        else:
            gears[(gear_x, gear_y)] = int(total)
    return (j, 0)
            

grid = []
file = open("input.txt", "r")
for line in file.readlines():
    section = []
    line = line.strip("\n")
    for char in line:
        section.append(char)
    grid.append(section)

sum = 0
i = 0

while (i < len(grid)):
    j = 0
    while (j < len(grid[0])):
        if(grid[i][j]) in digits:
            ret = helper(grid, i, j)
            j = ret[0]
            sum += ret[1]
        else:
            j += 1
    i += 1


print(sum)
        
