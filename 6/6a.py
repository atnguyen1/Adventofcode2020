#!/usr/bin/env python

import argparse
from functools import reduce
import sys


def main(args):
    """

    """
    custom_forms = None
    with open(args.input, 'r') as fh:
        custom_forms = fh.read()
        custom_forms = custom_forms.split('\n\n')

    total = 0
    for entry in custom_forms:
        answers = entry.split('\n')
        answers = [set(x) for x in answers]
        sum_group = reduce(lambda a, b: a.union(b), answers)
        total += len(sum_group)

    print(total)


if __name__ == '__main__':
    desc = 'Advent 6a'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
