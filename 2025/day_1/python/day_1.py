import numpy as np

def next_pos(current, movement, direction):
    '''
    take the current position, apply the movement and direction

    moving left below 0 needs to reset to 100 minus the difference
    moving right above zero needs to reset to 0 plus the difference
    '''

    if direction == 'R':
        pos = current + movement
    elif direction == 'L':
        pos = current - movement

    if abs(pos) > 99 or (pos < 0):
        pos = pos % 100

    return pos


def main():

    position = 50

    path = '../../input/day1_puzzle1.txt'
    #path = '../input/day1_puzzle1_example.txt'

    with open(path) as file:
        lines = [line.rstrip() for line in file]

    zero_counter = 0
    for l in lines:

        position = next_pos(position, int(l[1:]), l[0])

        if position == 0:
            zero_counter +=1
        print(f'Motion: {l}\nPosition: {position}')

    print(f'Number of times its hit zero: {zero_counter}')

if __name__ == '__main__':
    main()
