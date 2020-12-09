#!/usr/bin/env python

import argparse
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
    seat_ids = list()

    with open(args.input, 'r') as fh:
        for line in fh:
            line = line.rstrip()
            boarding_passes.append(line)

    for bp in boarding_passes:
        row, column = determine_seat(bp)
        seat_id = (row * 8) + column
        seat_ids.append(seat_id)

    print(sorted(seat_ids)[0])


if __name__ == '__main__':
    desc = 'Advent 5a'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
