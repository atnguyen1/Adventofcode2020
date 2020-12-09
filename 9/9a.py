#!/usr/bin/env python3

import argparse


def main(args):
    """
    """
    encodings = list()
    with open(args.input, 'r') as fh:
        encodings = fh.read().split('\n')
        encodings = [int(x) for x in encodings]

    data_ptr = 25

    while data_ptr < len(encodings):
        value = encodings[data_ptr]
        preamble = sorted(encodings[data_ptr - 25:data_ptr])

        found_value = False
        for p in preamble:
            if value - p in preamble:
                found_value = True
                break

        if found_value:
            data_ptr += 1
        else:
            print(value)
            break


if __name__ == '__main__':
    desc = 'Advent 9a'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
