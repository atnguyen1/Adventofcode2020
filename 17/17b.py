#!/usr/bin/env python3

import argparse
import copy
import numpy as np
import re
import math
import sys


np.set_printoptions(threshold=sys.maxsize)


class Cubeoflife():
    def __init__(self, pattern):
        # Puzzle input is 8 x 8
        # 6 cycles lets expansion go to max 14 as you iterate
        # 1 more
        self.zdim = 24
        self.ydim = 24
        self.xdim = 24
        self.wdim = 24
        self.space = np.zeros((self.wdim, self.zdim, self.ydim, self.xdim), dtype=int)
        zo = math.floor(self.zdim / 2)
        yo = math.floor(self.ydim / 2)
        xo = math.floor(self.xdim / 2)
        wo = math.floor(self.wdim / 2)
        origin = [wo, zo, yo, xo]    # z, y, x

        ylen = len(pattern)
        xlen = len(pattern[0])
        # print(ylen, xlen)
        xoffset = math.floor(xlen / 2.0)
        yoffset = math.floor(ylen / 2.0)
        # print(xoffset, yoffset)

        # print(pattern)
        for k, p in enumerate(pattern):
            # Compute starting locations
            w = origin[0]
            z = origin[1]
            y = origin[2] - yoffset + k
            x1 = origin[3] - xoffset
            x2 = x1 + len(p)
            # print(z, y , x1)
            self.space[w, z, y, x1:x2] = p

    def getneighbors(self, wi, zi, yi, xi):
        neighbor_states = list()     # 80 states
        for w in [-1, 0, 1]:
            for z in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    for x in [-1, 0, 1]:
                        if (x == 0) and (y == 0) and (z == 0) and (w == 0):
                            continue
                        if self.space[wi + w, zi + z, yi + y, xi + x] == 1:
                            neighbor_states.append(1)
                        else:
                            neighbor_states.append(0)
        return neighbor_states

    def cycle(self, count):
        for i in range(count):
            new_space = copy.deepcopy(self.space)
            for w in range(1, self.wdim - 1):
                for z in range(1, self.zdim - 1):
                    for y in range(1, self.ydim - 1):
                        for x in range(1, self.xdim - 1):
                            n = self.getneighbors(w, z, y, x)
                            n = sum(n)
                            # new_space[z, y, x] = n
                            if self.space[w, z, y, x] == 1:
                                # Check to flip off
                                if ((n == 2) or (n == 3)):
                                    # new_space[z, y, x] = 1
                                    new_space[w, z, y, x] = 1
                                else:
                                    new_space[w, z, y, x] = 0
                            else:
                                # Check to flip on
                                if n == 3:
                                    new_space[w, z, y, x] = 1
            self.space = new_space

    def print(self, z):
        print(self.space[w, z,::])


    def sumcubes(self):
        s = 0
        for w in range(0, self.wdim):
            for z in range(0, self.zdim):
                for y in range(0, self.ydim):
                    for x in range(0, self.xdim):
                        if self.space[w, z, y, x] == 1:
                            s += 1
        return s


def main(args):
    """
    """

    with open(args.input, 'r') as fh:
        init = fh.read().split('\n')
        updated = list()

        for i in init:
            i = i.replace('.', '0').replace('#', '1')
            i = [int(a) for a in i]
            updated.append(i)

        a = Cubeoflife(updated)
        a.cycle(6)
        print(a.sumcubes())
        '''
        print('Init')
        a.print(12)
        print('Cycle 1')
        a.cycle(1)
        a.print(11)
        a.print(12)
        a.print(13)
        print('Cycle 2')
        a.cycle(1)
        a.print(10)
        a.print(11)
        a.print(12)
        a.print(13)
        a.print(14)
        print('Cycle 3')
        a.cycle(1)
        a.print(10)
        a.print(11)
        a.print(12)
        a.print(13)
        a.print(14)
        '''

if __name__ == '__main__':
    desc = 'Advent 17b'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
