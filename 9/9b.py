#!/usr/bin/env python3

import argparse
from itertools import accumulate
import operator
import sys


def main(args):
    """
    """
    # From Part 1
    key = 375054920

    encodings = list()
    with open(args.input, 'r') as fh:
        encodings = fh.read().split('\n')
        encodings = [int(x) for x in encodings]

    for z in range(0, len(encodings) + 1):
        sums = accumulate(encodings[z:], func=operator.add)
        sums = list(sums)

        if key in sums:
            accumulate_position = sums.index(key)
            corrected_range = encodings[z:accumulate_position + z + 1]
            minimum = min(corrected_range)
            maximum = max(corrected_range)
            print(minimum, maximum, minimum + maximum)
            sys.exit()


if __name__ == '__main__':
    desc = 'Advent 9b'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
