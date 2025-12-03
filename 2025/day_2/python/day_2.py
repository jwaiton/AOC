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

def find_duplicate_substrings(value):
    '''
    checks if any duplicate substrings exist within a value
    REALISATION: this is not what the problem wants
    '''
    # extract all possible substrings
    substrings = [value[i:j] for i in range(len(value)) for j in range(i+1, len(value)+1)]
    # find duplicates, O(n*n) but who cares
    duplicates = set([x for x in substrings if substrings.count(x) > 1])

    # return invalid id to add if there are duplicates
    if len(duplicates) != 0:
        print(f'Invalid id of {value}')
        return int(value)
    else:
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
    path = '../../input/day2_puzzle1_example.txt'
    path = '../../input/day2_puzzle1.txt'
    bound_generator = interpret_data(path)

    duplicated_added = 0

    for lower_bound, upper_bound in bound_generator:
        #print(f'Lower bound: {lower_bound}, Upper bound: {upper_bound}')

        for i in range(lower_bound, upper_bound + 1):
            #duplicated_added += find_duplicate_substrings(str(i))
            duplicated_added += find_doublet_IDs(str(i))



    print(f'Sum of invalid IDs: {duplicated_added}')
if __name__ == '__main__':
    main()
