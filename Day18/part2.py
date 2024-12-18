#!/usr/bin/env python3
from numpy import full, array, ndenumerate


def water_method(maze):
    step = 0
    maze[0][0] = 'O'
    while maze[(maze.shape[0]-1, maze.shape[1] -1)] != 'O':
        step = step + 1
        steps = set()
        for index, element in ndenumerate(maze):
            if element == '#':
                continue
            if element == 'O':
                continue
            if index[0] > 0 and maze[index[0]-1][index[1]] == 'O':
                steps.add(index)
                maze[index] = 'O'
            if index[1] > 0 and maze[index[0]][index[1]-1] == 'O':
                steps.add(index)
                maze[index] = 'O'
            if index[0] < maze.shape[0]-1  and maze[index[0]+1][index[1]] == 'O':
                steps.add(index)
                maze[index] = 'O'
            if index[1] < maze.shape[1]-1 and maze[index[0]][index[1]+1] == 'O':
                steps.add(index)
                maze[index] = 'O'

        if len(steps) == 0:
            print(f"Unreachable")
            return False
    return True

if __name__ == "__main__":
    falling_bytes = list()
    with open('input.txt') as file:
        for line in file:
            falling_bytes.append( tuple(map(int, line.rstrip().split(',') ) ) )

    print(falling_bytes)
    
    the_grid = full((71,71), '.')
    
    print(the_grid)

    for x, y in falling_bytes[:1024]:
        the_grid[y][x] = '#'
    
    print(the_grid)

    print(f"1024: {water_method(the_grid.copy())}")
    
    for x, y in falling_bytes[1024:]:
        the_grid[y][x] = '#'
        print(f"Falling @ {x},{y}")
        print(the_grid)

        if not water_method(the_grid.copy()):
            print(f"Unreachable: {x},{y}")
            break


    


