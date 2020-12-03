#!/usr/bin/env python

import argparse
import sys

def main(args):
    field = list()
    x_pos = 0
    y_pos = 0
    tree_count = 0

    x_walk = 3
    y_walk = 1

    with open(args.input, 'r') as fh:
        for line in fh:
            line = line.rstrip()
            line = [x for x in line]
            field.append(line)

    x_pos += x_walk
    y_pos += y_walk



    while y_pos < len(field):
        # print('S', ''.join(field[y_pos - 1]))
        # print('S', ''.join(field[y_pos]))
        # print('')

        # print('T', ''.join(field[y_pos]))
        outx = ''
        for z, x in enumerate(field[y_pos]):
            if z == x_pos:
                outx += '?'
            else:
                outx += field[y_pos][z]
        # print('T', outx)
        # print('')

        if field[y_pos][x_pos] == '#':
            tree_count += 1

        if x_pos + x_walk > len(field[0]) - 1:
            x_pos = (x_pos + x_walk) - len(field[0])
        else:
            x_pos += x_walk
        y_pos += 1

    print("Trees", tree_count)


if __name__ == '__main__':
    desc = 'Advent 3a'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
