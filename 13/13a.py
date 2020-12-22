#!/usr/bin/env python3

import argparse
import numpy as np
from collections import Counter
import sys

np.set_printoptions(threshold=sys.maxsize)


class ship:
    def __init__(self, directions):
        pass

    def chugchug(self):
        pass

def closest(n, m):
    # For digit N, find closest integer divisible by m
    q = int(n / m)
    return m * q


def main(args):
    """
    """
    with open(args.input, 'r') as fh:
        earliest_departure = int(fh.readline())
        buses = fh.readline().split(',')

        bus_lines = list()
        for b in buses:
            if b == 'x':
                continue
            bus_lines.append(int(b))

        # print(earliest_departure)
        time_table = dict()
        for b in bus_lines:
            close = closest(earliest_departure, b)
            if close < earliest_departure:
                close += b

            time_table[b] = close

        smallest = earliest_departure * 2
        smallest_bus = None
        for t in time_table:
            et = time_table[t]

            if et <= smallest:
                smallest = et
                smallest_bus = t

        #print(smallest, smallest_bus, smallest - earliest_departure, (smallest - earliest_departure) * smallest_bus)
        print((smallest - earliest_departure) * smallest_bus)


if __name__ == '__main__':
    desc = 'Advent 13a'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
