#!/usr/bin/env python

import argparse


def main(args):
    costs = list()
    with open(args.input, 'r') as fh:
        for line in fh:
            line = line.rstrip()
            costs.append(int(line))

    sums = list()
    for entry in costs:
        diff = 2020 - entry
        if diff in costs:
            print(diff, entry, diff * entry)
            break


if __name__ == '__main__':
    desc = 'Advent 1a'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
