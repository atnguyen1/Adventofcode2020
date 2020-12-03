#!/usr/bin/env python

import argparse
import sys

def main(args):
    field = list()

    walks = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    with open(args.input, 'r') as fh:
        for line in fh:
            line = line.rstrip()
            line = [x for x in line]
            field.append(line)

    tree_walk_count = list()
    for entry in walks:
        x_walk = entry[0]
        y_walk = entry[1]

        print(entry)

        tree_count = 0
        x_pos = 0
        y_pos = 0

        x_pos += x_walk
        y_pos += y_walk

        while y_pos < len(field):
            '''
            print('S', ''.join(field[y_pos - 1]))
            print('S', ''.join(field[y_pos]))
            if y_pos != len(field) - 1:
                print('S', ''.join(field[y_pos + 1]))
            print('')
            '''

            # print('T', ''.join(field[y_pos - 1]))
            outx = ''
            for z, x in enumerate(field[y_pos]):
                if z == x_pos:
                    outx += '?'
                else:
                    outx += field[y_pos][z]
            # print('T', outx)
            # if y_pos != len(field) - 1:
            #     print('T', ''.join(field[y_pos + 1]))
            # print('')

            if field[y_pos][x_pos] == '#':
                tree_count += 1

            if x_pos + x_walk > len(field[0]) - 1:
                x_pos = (x_pos + x_walk) - len(field[0])
            else:
                x_pos += x_walk
            y_pos += y_walk

        tree_walk_count.append(tree_count)

    print(tree_walk_count)
    mult = 1
    for entry in tree_walk_count:
        mult = mult * entry

    print(mult)


if __name__ == '__main__':
    desc = 'Advent 3a'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
