#!/usr/bin/env python

import argparse


def main(args):
    costs = list()
    with open(args.input, 'r') as fh:
        for line in fh:
            line = line.rstrip()
            costs.append(int(line))

    for z, entry in enumerate(costs):
        diff1 = 2020 - entry

        for y, entry2 in enumerate(costs):
            if y == z:
                continue
            diff2 = diff1 - entry2

            if diff2 in costs:
                if entry + entry2 + diff2 == 2020:
                    print(entry, entry2, diff2, entry * entry2 * diff2)


if __name__ == '__main__':
    desc = 'Advent 1a'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
