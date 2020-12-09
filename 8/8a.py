#!/usr/bin/env python

import argparse
import re
import sys


def main(args):
    """
    """

    accumulator = 0
    op_pointer = 0

    visited = list()
    code = list()

    with open(args.input, 'r') as fh:
        code = fh.read().split('\n')

    halt = False
    while not halt:
        op, val = code[op_pointer].split(' ')
        val = int(val)
        # print(op, val)

        if op_pointer in visited:
            halt = True
            print('Accumulator', accumulator)
            sys.exit()

        visited.append(op_pointer)

        if op == 'acc':
            accumulator += val
            op_pointer += 1
        elif op == 'jmp':
            op_pointer += val
        elif op == 'nop':
            op_pointer += 1
        else:
            print('OP ERROR', code[op_pointer])
            sys.exit()



if __name__ == '__main__':
    desc = 'Advent 8a'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
