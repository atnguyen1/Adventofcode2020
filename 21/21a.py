#!/usr/bin/env python3

import argparse
import re
from collections import defaultdict
from hopcroftkarp import HopcroftKarp
import sys


def main(args):
    """
    """
    with open(args.input, 'r') as fh:
        data = fh.read().split('\n')
        allergens_map = defaultdict(list)
        all_ingred = list()

        for d in data:
            res = re.match('(.+)\(contains(.+)\)', d)

            if res:
                ingredients = res.group(1).rstrip().lstrip().split(' ')
                allergens = res.group(2).rstrip().lstrip().split(', ')

                for a in allergens:
                    allergens_map[a].append(set(ingredients))
                all_ingred.append(ingredients)

        poison = list()
        graph = {}
        for a in allergens_map:
            i = set.intersection(*allergens_map[a])
            graph[a] = i
            for entry in i:
                if entry not in poison:
                    poison.append(entry)

        # print(all_ingred)
        c = 0
        for a in all_ingred:
            for i in a:
                if i not in poison:
                    c += 1
        print(c)

        # matcb = HopcroftKarp(food).maximum_matching(keys_only=True)
        # k = matcb.keys()


if __name__ == '__main__':
    desc = 'Advent 21a'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
