#!/usr/bin/env python3

import argparse
import re
import sys


def main(args):
    """
    """
    visited = list()
    code = list()

    with open(args.input, 'r') as fh:
        code = fh.read().split('\n')

    original_code = code.copy()

    # Iteratively change 1 line of code
    for z, c in enumerate(code):
        opx, valx = c.split(' ')
        newop = ''
        if opx == 'jmp':
            newop = 'nop ' + valx
        elif opx == 'nop':
            newop = 'jmp ' + valx
        else:
            continue

        code[z] = newop

        accumulator = 0
        op_pointer = 0

        visited = list()
        halt = False
        loop = False

        while not halt:
            if op_pointer in visited:
                halt = True
                loop = True
                # print('Accumulator', accumulator)
                break
            elif op_pointer >= len(code):
                halt = True
                break

            op, val = code[op_pointer].split(' ')
            val = int(val)

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

        if loop:
            # We repeated instructions reset code
            code = original_code.copy()
        else:
            # We completed operations
            print('Accumulator Complete', accumulator)
            sys.exit()


if __name__ == '__main__':
    desc = 'Advent 8a'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
