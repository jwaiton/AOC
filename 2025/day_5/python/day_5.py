'''
ingredient catastrophe!
whats fresh and whats spoilt?
'''
from tqdm import tqdm

def parse_lines(lines):
    '''
    separate based on the '' element in the list
    '''

    fresh = lines[0:lines.index('')]
    available = lines[lines.index('')+1:len(lines)]
    return fresh, available

def return_fresh(region):
    '''
    takes string of range ('3-5') and returns the set of those values {3,4,5}
    '''
    fresh_set = set()
    vals = region.split('-')
    #print(vals)
    for i in range(int(vals[0]), int(vals[1])+1):
        fresh_set.add(i)

    #print(f'Set: {fresh_set}')
    return fresh_set


if __name__ == '__main__':

    #path = '../../input/day5_puzzle1_example.txt'
    path = '../../input/day5_puzzle1.txt'

    with open(path) as file:
        lines = [line.rstrip() for line in file]

    fresh, available = parse_lines(lines)

    full_fresh_set = set()
    for f in tqdm(fresh):
        # create set of all ids that are fresh
        full_fresh_set = full_fresh_set.union(return_fresh(f))

    #print(f'Full fresh set: {full_fresh_set}')

    total_available = 0
    for a in tqdm(available):
        #print(a)
        if int(a) in full_fresh_set:
            total_available += 1

    print(f'Total fresh and available ingredients: {total_available}')
