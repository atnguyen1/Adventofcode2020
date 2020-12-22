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
    # test = nums


    turns = 2021
    turns = 30000001
    current_turn = len(test) + 1
    start = True

    while current_turn < turns:
        last_num = test[-1]

        if start:
            test.append(0)
            start = False
            # print(test)
            # print(current_turn)
            current_turn += 1
            continue
        else:
            if test.index(last_num) == len(test) - 1:
                # Unique Number
                test.append(0)
                current_turn += 1
                # print(current_turn, test)
                continue

            # Else has multiple occurences
            last_apperance_list = [i for i, x in enumerate(test) if x == last_num]
            last = last_apperance_list[-1] + 1
            penultimate = last_apperance_list[-2] + 1
            # print(last_apperance_list, last, penultimate)
            test.append(last - penultimate)

        current_turn += 1
        # print(current_turn, test)

    print(test[-1])


if __name__ == '__main__':
    desc = 'Advent 15a'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
