#!/usr/bin/env python3

import argparse
import numpy as np
from collections import Counter
import sys

np.set_printoptions(threshold=sys.maxsize)


class ship:
    def __init__(self, directions):
        self.currentx = 0
        self.currenty = 0
        self.facing = 'E'
        self.directions = directions
        self.direction_index = 0

    def chugchug(self):
        for d in self.directions:
            direct = d[0]
            value = int(d[1:])

            if direct in ['N', 'E', 'S', 'W']:
                self.move(direct, value)
            elif direct in ['L', 'R']:
                self.rotate(direct, value)
            elif direct == 'F':
                self.move(self.facing, value)
            else:
                print('Invalid command', d, file=sys.stderr)
                sys.exit()

    def chug(self):
        d = self.directions[self.direction_index]
        direct = d[0]
        value = int(d[1:])
        self.direction_index += 1

        if direct in ['N', 'E', 'S', 'W']:
            self.move(direct, value)
        elif direct in ['L', 'R']:
            self.rotate(direct, value)
        elif direct == 'F':
            self.move(self.facing, value)
        else:
            print('Invalid command', d, file=sys.stderr)
            sys.exit()

    def move(self, direction, value):
        # Easy directions
        if direction == 'N':
            self.currenty += value
        elif direction == 'S':
            self.currenty -= value
        elif direction == 'W':
            self.currentx -= value
        elif direction == 'E':
            self.currentx += value
        else:
            print('Invalid Move', direction, value, file=sys.stderr)
            sys.exit()

    def rotate(self, direction, value):
        clockwise = ['N', 'E', 'S', 'W']
        counterclock = ['N', 'W', 'S', 'E']

        steps = int(value / 90)
        if direction == 'R':
            current_direction = clockwise.index(self.facing)
        elif direction == 'L':
            current_direction = counterclock.index(self.facing)

        adjusted_dir = current_direction + steps
        adjusted_dir = int(adjusted_dir % 4)

        if direction == 'L':
            # Counter clockwise
            # Step backward through list steps time
            adjusted_dir = counterclock[adjusted_dir]
        elif direction == 'R':
            # Clockwise
            # Step forward through list steps time
            adjusted_dir = clockwise[adjusted_dir]
        else:
            print('Invalid Direction', direction, value, file=sys.stderr)
            sys.exit()

        self.facing = adjusted_dir

    def manahatten(self):
        return abs(self.currentx) + abs(self.currenty)

    def getfacing(self):
        return self.facing

    def getxy(self):
        # X, Y
        return self.currentx, self.currenty


def main(args):
    """
    """
    nav = list()
    with open(args.input, 'r') as fh:
        nav = fh.read().split('\n')

    s = ship(nav)
    s.chugchug()
    print(s.manahatten())



if __name__ == '__main__':
    desc = 'Advent 12a'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
