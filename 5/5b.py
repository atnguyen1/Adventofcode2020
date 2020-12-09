#!/usr/bin/env python

import argparse
import numpy as np
import sys


def determine_seat(encoding):
    height = range(0, 128)
    width = range(0,8)

    row = encoding[:7]
    columns = encoding[7:]

    for char in row:
        if char == 'F':
            height = height[:len(height) / 2]
        elif char == 'B':
            height = height[len(height) / 2:]

    for char2 in columns:
        if char2 == 'L':
            width = width[:len(width) / 2]
        elif char2 == 'R':
            width = width[len(width) / 2:]

    return height[0], width[0]


def main(args):
    """

    """
    boarding_passes = list()
    seats = list()

    # np.set_printoptions(threshold=sys.maxsize)


    with open(args.input, 'r') as fh:
        for line in fh:
            line = line.rstrip()
            boarding_passes.append(line)

    for bp in boarding_passes:
        row, column = determine_seat(bp)
        seat = (int(row), int(column))
        seats.append(seat)

    plane = np.zeros((128, 8))

    for row, column in seats:
        plane[row, column] = 5

    # unfilled_seats = list()
    for y in range(0, 128):
        for x in range(0, 7):
            if plane[y, x] == 0:
                if x == 0 or x == 7:
                    continue
                if plane[y, x - 1] == 5 and plane[y, x + 1] == 5:
                    #unfilled_seats.append((y, x))
                    print((y * 8) + x)

    # print(unfilled_seats)



if __name__ == '__main__':
    desc = 'Advent 5a'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
