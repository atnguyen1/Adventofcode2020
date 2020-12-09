#!/usr/bin/env python

import argparse
from functools import reduce
import re
import sys


def find_color(data, color):
    bags = []

    for k in data:
        if color in data[k]:
            bags.append(k)

    return bags


def main(args):
    """
    """
    rules = dict()
    baggage = dict()

    with open(args.input, 'r') as fh:
        d = fh.read()
        rules = d.split('\n')

    # store baggage rules
    for r in rules:
        (bag, contents) = r.split(' bags contain ')
        baggage[bag] = dict()
        if contents == 'no other bags.':
            # bag contents is the empty dictionary
            continue
        for c in contents.split(','):
            c = c.rstrip().lstrip()
            r = re.match('(\d+) (\w+ \w+) bag.*', c)
            count, color = r.groups()
            baggage[bag][color] = int(count)

    gold_containers = find_color(baggage, 'shiny gold')

    # Grab all bags that contain the a bag that can hold gold 
    for g in gold_containers:
        gold_containers += find_color(baggage, g)

    print(set(gold_containers))
    print(len(set(gold_containers)))


if __name__ == '__main__':
    desc = 'Advent 7a'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
