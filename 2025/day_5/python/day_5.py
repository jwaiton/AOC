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


def check_fresh_range(region : str, available : int):
    '''
    takes all region ranges and checks if the value falls within it, if so
    set to true
    '''
    lower, upper = region.split('-')
    if (int(available)>= int(lower)) and (int(available) <= int(upper)):
        return 1
    else:
        return 0

if __name__ == '__main__':

    #path = '../../input/day5_puzzle1_example.txt'
    path = '../../input/day5_puzzle1.txt'

    with open(path) as file:
        lines = [line.rstrip() for line in file]

    fresh, available = parse_lines(lines)


    total_available = 0
    for a in tqdm(available):

        for f in fresh:
            if check_fresh_range(f,a) == 1:
                print(f'Fresh {a} in {f}')
                total_available += 1
                break


    print(f'Total fresh and available ingredients: {total_available}')
