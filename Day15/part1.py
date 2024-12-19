#!/usr/bin/env python3
from numpy import where, array, ndenumerate

_direction = dict()
_direction['>'] = (0, +1)
_direction['<'] = (0, -1)
_direction['^'] = (-1, 0)
_direction['v'] = (+1, 0)

def move(cursor, direction):
    return (cursor[0] + _direction[direction][0], cursor[1] + _direction[direction][1])

def try_move(warehouse, item, direction):
    update = move(item, direction)
    print(f"try to move {direction} {warehouse[item]}{item} to {warehouse[update]}{update}")
    if warehouse[update] == '#':
        return False
    if warehouse[update] == '.':
        warehouse[update] = warehouse[item]
        warehouse[item] = '.'
        item = update
        return True
    if warehouse[update] == 'O':
        if try_move(warehouse, update, direction):
            warehouse[update] = warehouse[item]
            warehouse[item] = '.'
            item = update
            return True
        return False
    raise Exception('Unidentified Item')

def calc_warehouse_value(warehouse):
    value = 0
    for index, item in ndenumerate(warehouse):
        if item == 'O':
            value = value + (100 * index[0]) + (index[1])
    return value


if __name__ == "__main__":
    warehouse = []
    moves = []

    with open('input.txt') as file:
        for line in file:
            if line.startswith('#'):
                warehouse.append([x for x in line.rstrip()])
            if line[0] in ['<','v','^','>']:
                moves.extend([x for x in line.rstrip()])
        warehouse = array(warehouse)

    print(f"WAREHOUSE")
    print(warehouse)

    for index, element in ndenumerate(warehouse):
        if element == '@':
            ROBOT = index

    print(f"Robot is at {ROBOT}")
    print("===== START =====")
    for m in moves:
        if try_move(warehouse, ROBOT, m):
            ROBOT = move(ROBOT, m)
            
        print(warehouse)
        print(f"Robot is at {ROBOT}")
        print()
    
    print()
    value = calc_warehouse_value(warehouse)
    print(f"Warehouse Value = {value}")

