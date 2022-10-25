# Utility to check if the current cell position (x,y)
# is in the maze
def isSafe(maze, x, y, sol):
    # Get maze dimensions
    X = len(maze[1])
    Y = len(maze)

    if x>=0 and x<X and y>=0 and y<Y and maze[x][y]==1:    
        return True
    return False

# (x,y) is the current cell position
def solveMaze(maze, x, y, sol):

    # Get maze size
    X = len(maze[1])
    Y = len(maze)

    # check if (x,y) is goal
    if x == X-1 and y == Y-1 : 
        sol[x][y] = 1
        return True

    # Check if we're inside the maze
    if isSafe(maze, x, y, sol):
        # Mark the current cell in solution (BACKTRACK)
        sol[x][y] = 1
        # Move right
        if solveMaze(maze, x+1, y, sol):
            return True
        # Move down
        if solveMaze(maze, x, y+1, sol):
            return True
        # Remove current cell from solution
        # If the 2 moves above failed
        sol[x][y] = 0
        return False

maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1,]
]
# Initiate the solution matrix
sol = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Given a maze NxM,
# we start at (0, 0), goal is (N-1, M-1)
if solveMaze(maze, 0, 0, sol):
    print sol
else:
    print "No solution"