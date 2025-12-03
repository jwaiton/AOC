import numpy as np




def next_pos(current, movement, direction):
    '''
    the iterator method, no intelligence pure brute force
    '''

    # number of rotations
    rotations = 0

    if direction == 'R':
        direction = 1
    elif direction == 'L':
        direction  = -1

    for i in range(movement):
        current += direction

        # the boundaries
        if current == -1:
            current = 99
        if current == 100:
            current = 0

        # the counter
        if current == 0:
            rotations += 1




    return current, rotations


def main():

    position = 50

    path = '../../input/day1_puzzle1.txt'
    #path = '../input/day1_puzzle1_example.txt'
    #path = '../input/day1_puzzle1_example2.txt'
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    rotation_counter = 0
    zero_counter = 0
    for l in lines:
        position, rotations = next_pos(position, int(l[1:]), l[0])
        rotation_counter += rotations
    print(f'Hit zero {zero_counter} times.')
    print(f'Rotated {rotation_counter} number of times')

if __name__ == '__main__':
    main()
