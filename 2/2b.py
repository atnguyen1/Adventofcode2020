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
                pos1 = int(res.group(1))
                pos2 = int(res.group(2))
                letter = res.group(3)
                password = res.group(4)

                if ((password[pos1 - 1] == letter) and (password[pos2 - 1] != letter)):
                    valid += 1
                elif ((password[pos2 - 1] == letter) and (password[pos1 - 1] != letter)):
                    valid += 1
                else:
                    invalid += 1

                # print(line, min_len, max_len, letter, res.group(4), password)
            else:
                print('RE failure', line)

        print('Valid', valid)
        print('Invalid', invalid)


if __name__ == '__main__':
    desc = 'Advent 2b'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
