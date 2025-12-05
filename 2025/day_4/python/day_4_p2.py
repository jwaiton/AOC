'''
rolls of paper, a NN question basically

How many NN does each roll have?
Less then 4? Can be picked up.
More than 4? Can't be picked up.
'''



import numpy as np
def generate_2D_array(data):
    '''
    alter the given array to:
    @ --> 1
    . --> 0
    '''
    x = np.array([[0 if char == '.' else 1 for char in row] for row in data])
    return x


def NN_count(array):
    '''
    given a 2D array of rolls of paper, how many NN do they have
    '''

    # roll in each direction, add the sum
    NN = np.roll(array, 1, axis = 1) + np.roll(array, -1, axis = 1) + np.roll(array, 1, axis = 0) + np.roll(array, -1, axis = 0)
    # diagonals
    NN += np.roll(array, (1, 1), axis = (0,1)) + np.roll(array, (-1, -1), axis = (0, 1)) + np.roll(array, (-1, 1), axis = (0,1)) + np.roll(array, (1, -1), axis = (0,1))


    return NN

if __name__ == '__main__':
    #path = '../../input/day4_puzzle1_example.txt'
    path = '../../input/day4_puzzle1.txt'

    with open(path) as file:
        lines = [line.rstrip() for line in file]

    x = generate_2D_array(lines)
    print(x)
    rolls_removed = -1
    total_rolls_removed = 0

    while rolls_removed != 0:
        # make a 2d array
        print('=' * 20)

        # pad
        padded_x = np.pad(x, pad_width = 1, mode = 'constant', constant_values = (0))
        # count nearest neighbours
        NN = NN_count(padded_x)
        # strip the edges
        NN = NN[1:-1, 1:-1]
        # mask for values greater than 4
        less_than_four = NN < 4
        # only take things less than four that were rolls
        rolls_less_than_four = np.logical_and(less_than_four, x.astype(bool))

        rolls_removed = np.sum(rolls_less_than_four.astype(int))
        total_rolls_removed += rolls_removed
        print(f'rolls removed {rolls_removed}')
        # remove the rolls!
        x = x - rolls_less_than_four.astype(int)
        print(x)

    print(f'Total rolls removed: {total_rolls_removed}')

