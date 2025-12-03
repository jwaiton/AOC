


def maximal_joltage(bank : str):
    '''
    from an individual battery bank
    eg: '11123456'
    collect the largest possible voltage (no reordering)
    eg: '56'
    '''

    max_power = 0

    # the dumbest way possible, brute force my friend!
    for num_i, i in enumerate(bank):
        for num_j, j in enumerate(bank):

            if num_i >= num_j:
                continue
            #print('=')
            #print(i)
            #print(j)
            #print('=')
            test_power = int(i + j)
            if test_power > max_power:
                print(f'new max power: {test_power} beating {max_power}')
                max_power = test_power

    print(f'Max: {max_power}')
    return max_power

if __name__ == '__main__':
    #path = '../../input/day3_puzzle1_example.txt'
    path = '../../input/day3_puzzle1.txt'

    summed_joltage = 0

    with open(path) as file:
        # read in the lines
        lines = [line.rstrip() for line in file]

    for bank in lines:
        print('=' * 20)
        print(f'{bank}')
        summed_joltage += maximal_joltage(bank)

    print(summed_joltage)
