#!/usr/bin/env python3

import argparse
from bitarray import bitarray
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
        masked_value = self.getmaskvalue(value)
        self.memory[address] = int(masked_value, 2)

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
                mod_value.append(value[z])
            elif char == '0':
                mod_value.append('0')
            elif char == '1':
                mod_value.append('1')

        return(''.join(mod_value))        

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
    desc = 'Advent 13a'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
