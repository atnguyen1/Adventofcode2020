#!/usr/bin/env python3

import argparse
import numpy as np
from collections import Counter
import sys

np.set_printoptions(threshold=sys.maxsize)


class gameoflife:
    def __init__(self, input_grid):
        # . = ground == 0
        # L = seat == 1
        # # = occupied == 2

        self.raw_input = input_grid
        self.state = list()

        self.ybound = len(input_grid)
        self.xbound = len(input_grid)

        # Construct grid that has 1x padding on all sides to avoid bounds

        # Top Row
        self.state.append([-1 for x in range(self.xbound + 2)])

        for r in input_grid:
            r = [int(x) for x in r.replace('.', '0').replace('L', '1')]
            r = [-1] + r + [-1]
            self.state.append(r)

        # Bottom Row
        self.state.append([-1 for x in range(self.xbound + 2)])

        self.state = np.array(self.state)
        self.previous_state = np.array([0])


    def iterate_once(self):
        # Use a new copy to fill seats, swap at the end
        new_state_matrix = self.state.copy()

        for (y, x), s in np.ndenumerate(self.state):
            # Ignore cells on border
            if y == 0:
                continue
            if x == 0:
                continue
            if y == len(self.state) - 1:
                continue
            if x == len(self.state[0]) - 1:
                continue

            if self.state[y, x] == 0:
                # Ground
                continue

            seat_counts = self.free(y, x)
            if seat_counts[False] == 0:
                new_state_matrix[y, x] = 2
            elif seat_counts[False] >= 4:
                new_state_matrix[y, x] = 1

        self.previous_state = self.state
        self.state = new_state_matrix


    def iterate_stable(self):
        current_seats = self.get_filled_seats()
        previous_seats = -1

        while current_seats != previous_seats:
            self.iterate_once()
            previous_seats = current_seats
            current_seats = self.get_filled_seats()


    def free(self, y, x):
        # Check the following cells
        # 1 2 3
        # 4   5
        # 6 7 8
        # Check in numerical order
        seats_free = list()
        for j in [-1, 0, 1]:
            for i in [-1, 0 , 1]:
                # Don't check our x, y
                if i == 0 and j == 0:
                    continue
                if self.state[y + j, x + i] < 2:
                    seats_free.append(True)
                else:
                    seats_free.append(False)

        seat_counts = Counter(seats_free)
        return seat_counts


    def get_filled_seats(self):
        filled = 0
        for (y, x), val in np.ndenumerate(self.state):
            if val == 2:
                filled += 1
        return filled


    def print(self):
        for row in self.state:
            row2 = list()
            for r in row:
                if r == -1:
                    row2.append(0)
                else:
                    row2.append(r)
            row = [str(x) for x in row2]
            row = ''.join(row)
            row = row.replace('0', '.').replace('1', 'L').replace('2', '#')
            print(row)


def main(args):
    """
    """
    seats = list()
    with open(args.input, 'r') as fh:
        seats = fh.read().split('\n')

    b = gameoflife(seats)
    b.iterate_stable()
    b.print()
    print(b.get_filled_seats())




if __name__ == '__main__':
    desc = 'Advent 11a'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
