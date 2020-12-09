#!/usr/bin/env python

import argparse
import re
import sys


def find_color(data, color):
    bags = []

    for k in data:
        if color in data[k]:
            bags.append(k)

    return bags

def count_containing_bags(data, color):
    """
    Depth First Search Recursive
    """
    # print(path)
    total = 1

    if data[color] == {}:
        return total

    for c in data[color]:
        count = data[color][c]
        total += count * count_containing_bags(data, c)

    return total


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

    containers = baggage['shiny gold']

    # Walking a tree and multiplying nodes
    # Don't count root shiny gold bag
    s = count_containing_bags(baggage, 'shiny gold') - 1
    print(s)


if __name__ == '__main__':
    desc = 'Advent 7a'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
