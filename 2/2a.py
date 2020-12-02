#!/usr/bin/env python

import argparse
import re
import sys
from collections import Counter


def main(args):
    valid = 0
    invalid = 0
    with open(args.input, 'r') as fh:
        for line in fh:
            line = line.rstrip()
            res = re.match("(\d+)-(\d+).+(\w+): (\w+)", line)
            if res:
                # print(line)
                min_len = int(res.group(1))
                max_len = int(res.group(2))
                letter = res.group(3)
                password = Counter(res.group(4))

                letter_counts = password[letter]

                if (min_len <= letter_counts) and (letter_counts <= max_len):
                    valid += 1
                else:
                    invalid += 1

                # print(line, min_len, max_len, letter, res.group(4), password)
            else:
                print('RE failure', line)

        print('Valid', valid)
        print('Invalid', invalid)


if __name__ == '__main__':
    desc = 'Advent 2a'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
