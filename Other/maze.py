# 2d array of 0,1,6 representing a maze that your character can walk through
# 0 - represents empty space, the character can walk over empty space
# 1 - represents a wall, the character cannot walk over a wall
# 6 - represents a monster, the character can walk over a monster if you choose to but it will  lose a life
# a character that starts at position si, sj and tries to walk to ei, ej
# the character has N lives so it can walk over N-1 monsters	
# the character is allowed to walk on the 4 neighboring cells (up, down, left, right)

# return the shortest number of steps, -1 if impossible

# example grid

# g = [[0,1,0,0,0],
#      [0,6,0,1,0],
#      [0,0,0,1,0]]

# travel from 0,0 to 2,4
# 1 life  : shortest path length = ?
# 2 lives : shortest path length = ?
# 

grid =    [[0,0,6,0,1,0,0,0,0],
           [6,1,1,0,1,0,1,6,0],
           [0,1,0,0,1,0,1,0,0],
           [0,1,0,1,1,0,1,0,6],
           [0,1,0,0,1,0,6,0,0],
           [0,6,0,0,0,0,6,6,0]]

rows = len(grid)
cols = len(grid[0])

def shortest_path_helper(curi, curj, ei, ej, grid, lives, seen, curpath):
    if ([curi, curj] in seen):
        return 10000
    if curi < 0 or curi == rows or curj < 0 or curj == cols:
        return 10000
    if (grid[curi][curj] == 1):
        return 10000
    if (grid[curi][curj] == 6):
        lives -= 1
    if lives == 0:
        return 10000
    if (curi == ei and curj == ej):
        return curpath
    else:
        copy = seen.copy()
        copy.append([curi, curj])
        left = shortest_path_helper(curi, curj - 1, ei, ej, grid, lives, copy, curpath + 1)
        down =  shortest_path_helper(curi + 1, curj, ei, ej, grid, lives, copy, curpath + 1)
        right = shortest_path_helper(curi, curj + 1, ei, ej, grid, lives, copy, curpath + 1)
        up =  shortest_path_helper(curi - 1, curj, ei, ej, grid, lives, copy, curpath + 1)
        return min(
            left, right, up, down
        )
    
    
def shortest_path_length(si, sj, ei, ej, grid, lives):     
    ans = shortest_path_helper(si, sj, ei, ej, grid, lives, [], 0)
    return -1 if ans == 10000 else ans

assert shortest_path_length(0, 0, 5, 8, grid, 5) == 13
assert shortest_path_length(0, 0, 5, 8, grid, 4) == 15
assert shortest_path_length(0, 0, 5, 8, grid, 3) == 17
assert shortest_path_length(0, 0, 5, 8, grid, 2) == 27
assert shortest_path_length(0, 0, 5, 8, grid, 1) == -1

print("Success!")
