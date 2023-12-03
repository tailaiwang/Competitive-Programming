'''
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

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right).
Every other number is adjacent to a symbol and so is a part number; their sum is 4361.
'''

digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

def grid_check(grid, x, y):
    return True if x <= len(grid) - 1 and x >= 0 and y <= len(grid[0]) - 1 and y >= 0 else False

def helper(grid, i, j):
    valid = False
    total = ""
    while (grid_check(grid, i, j) and grid[i][j] in digits):
        for direction in directions:
            x = i + direction[0]
            y = j + direction[1]
            if grid_check(grid, x, y):
                if grid[x][y] not in digits and grid[x][y] != ".":
                    valid = True
        total += grid[i][j]
        j += 1
    print(total, valid)
    return (j, int(total)) if valid else (j, 0)
            

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
        
