import numpy as np



def interpret_data(path):
    '''
    yields ranges to test for invalid product ids
    '''

    with open(path) as file:
        lines = [line.rstrip().split(',') for line in file][0]
        bounds = ([x.split('-') for x in lines])
        for b in bounds:
            yield int(b[0]), int(b[1])

def find_repeaters(value):
    '''
    loop through the values, checking that each small substring doesnt duplicate throughout
    the rest of the string
    '''

    # extract list of substrings to check against the main string
    x = [(value[:i], value[i:]) for i, _ in enumerate(value)]

    #if value == '1010':
        #print(x)
    for i in x:
        #if value == '1010':
            #print(i)
        head = i[0]
        tail = i[1]
        #print(f'head: {head}, tail: {tail}')

        # must not be an empty substring
        if head == '' or tail == '':
            continue
        # must be divisible by the length of your substring
        if len(value) % len(head) != 0:
            continue
        # divide the remaining string up, if its a set it'll remove duplicates --> only one entry
        split_substring = set([tail[i:i+len(head)] for i in range(0, len(tail), len(head))] + [head])

        #if value == '1010':
        #    print(f'1010 diagnostics: head {head}, tail: {tail}\nsplit_substring: {split_substring}')

        if len(split_substring) == 1:
            print(f'{value} is a repeating sequence of {head}')
            #print(f'Diagnostics: head {head}, tail: {tail}\nsplit_substring: {split_substring}')
            return int(value)
        else:
            continue

    return 0

def find_doublet_IDs(value):
    '''
    what the problem actually wants:
    ID values consisting of IDs that are explicitly identical
    '''

    # odd number --> can't be made up of double digits
    if len(value) % 2 == 1:
        return 0

    # split in half
    if value[:len(value)//2] == value[len(value)//2:]:
        return int(value)
    else:
        return 0

def main():
    #path = '../../input/day2_puzzle1_example.txt'
    path = '../../input/day2_puzzle1.txt'
    bound_generator = interpret_data(path)

    duplicated_added = 0

    for lower_bound, upper_bound in bound_generator:
        #print(f'Lower bound: {lower_bound}, Upper bound: {upper_bound}')

        for i in range(lower_bound, upper_bound + 1):
            duplicated_added += find_repeaters(str(i))
            #duplicated_added += find_doublet_IDs(str(i))



    print(f'Sum of invalid IDs: {duplicated_added}')
if __name__ == '__main__':
    main()
