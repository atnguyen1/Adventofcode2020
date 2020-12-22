#!/usr/bin/env python3

import argparse
from collections import Counter
import sys



def main(args):
    """
    """
    nums = [6, 19, 0, 5, 7, 13, 1]
    test = [0, 3, 6]
    # test = [1, 3, 2]
    # test = [2, 1, 3]
    # test = [1, 2, 3]

    # test = [3, 1 ,2]
    test = nums

    # Store positions in dictionary
    position_lookup = dict(zip(test, [[z + 1] for z,i in enumerate(test)]))

    # turns = 2020
    turns = 30000000
    current_turn = len(test) + 1

    while current_turn <= turns:
        last_num = test[-1]  # Last spoken number

        if len(position_lookup[last_num]) == 1:
            # Element occured for first time
            test.append(0)
            position_lookup[0].append(current_turn)
            if len(position_lookup[0]) > 2:
                position_lookup[0] = position_lookup[0][-2:]
        else:
            try:
                positions = position_lookup[last_num]
                last = positions[-1]
                pen = positions[-2]
            except:
                print('Index Error', positions)
                sys.exit()

            dif = last - pen
            test.append(dif)
            if dif not in position_lookup:
                position_lookup[dif] = [current_turn]
            else:
                position_lookup[dif].append(current_turn)
            if len(position_lookup[dif]) > 2:
                position_lookup[dif] = position_lookup[dif][-2:]

        #print(current_turn, test), # position_lookup)
        current_turn += 1
        test = test[1:]

    print(test)
    print(test[-1])



if __name__ == '__main__':
    desc = 'Advent 15a'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
