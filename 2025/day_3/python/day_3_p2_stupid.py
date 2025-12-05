


def maximal_joltage(bank : str):
    '''
    checks the maximum in a given range,
    '''

    # convert into list of ints
    bank = [int(d) for d in bank]

    joltage       = ''
    start_index   = 0
    length        = len(bank)
    sub_bat_len  = 12
    # twelve digits
    for position in range(sub_bat_len):
        # determine the range over which to scan
        end_index            = length - (sub_bat_len - position) + 1
        # select max, ensure next step looks at values beyond current
        max_in_sub_bat = max(bank[start_index:end_index])
        start_index = bank.index(max_in_sub_bat, start_index, end_index) + 1
        joltage += str(max_in_sub_bat)

    return joltage
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
        summed_joltage += int(maximal_joltage(bank))

    print(summed_joltage)
