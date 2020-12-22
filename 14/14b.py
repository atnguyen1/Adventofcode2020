#!/usr/bin/env python3

import argparse
from bitarray import bitarray
from collections import deque
import numpy as np

import re
import sys


np.set_printoptions(threshold=sys.maxsize)

class Memory:
    def __init__(self):
        mask = ''
        self.memory = dict()    # Dictionary of memory addresses, memory address = bitarray

    def setmask(self, mask):
        mask = [m for m in mask]
        self.mask = mask

    def setmemory(self, address, value):
        masked_address = self.getmaskvalue(address)

        # Generate all address from masked_address
        address_permutations = deque([masked_address])

        compute = True
        while compute:

            seq = address_permutations.popleft()
            if 'X' in seq:
                idx = seq.index('X')

                for c in ['0', '1']:
                    enum = seq[:idx] + [c] + seq[idx + 1:]
                    address_permutations.append(enum)
            else:
                # Put it back if there are no X's
                address_permutations.appendleft(seq)
                compute = False

        for a in address_permutations:
            decoded = int(''.join(a), 2)
            # print(''.join(a), decoded)
            self.memory[decoded] = value


    def getmaskvalue(self, value):
        # Encode value into a string
        bitstring = "{0:b}".format(value)
        size = len(bitstring)
        padding = '0' * (36 - size)
        value = padding + bitstring
        value = [v for v in value]

        mod_value = list()

        for z,char in enumerate(self.mask):
            if char == 'X':
                mod_value.append('X')
            elif char == '0':
                mod_value.append(value[z])
            elif char == '1':
                mod_value.append('1')

        return(mod_value)

    def getmask(self):
        return self.mask

    def printmemory(self):
        print(self.memory)

    def sum_memory(self):
        s = 0
        for entry in self.memory:
            s += self.memory[entry]

        return s


def main(args):
    """
    """
    # 36-bit unsigned integers
    a = Memory()

    with open(args.input, 'r') as fh:
        for line in fh:
            line = line.rstrip()

            res = re.match('mask = (.+)', line)
            if res:
                a.setmask(res.group(1))
                continue

            res2 = re.match('mem\[(\d+)\] = (\d+)', line)
            if res2:
                a.setmemory(int(res2.group(1)), int(res2.group(2)))

    print(a.sum_memory())


if __name__ == '__main__':
    desc = 'Advent 14b'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
