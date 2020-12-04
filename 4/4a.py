#!/usr/bin/env python

import argparse
import sys


def main(args):
    """
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)
    """

    valid = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    passports = list()
    single_passport = dict()
    valid_count = 0
    invalid_count = 0

    with open(args.input, 'r') as fh:
        for line in fh:
            line = line.rstrip()
            if line == '':
                passports.append(single_passport)
                #print(single_passport)
                vflag = True
                for v in valid:
                    if v not in single_passport:
                        vflag = False

                if vflag is True:
                    valid_count += 1
                else:
                    invalid_count += 1

                single_passport = dict()
            else:
                data = line.rstrip().split(' ')
                for d in data:
                    k = d.split(':')[0]
                    v = d.split(':')[1]
                    single_passport[k] = v

        # Handle last entry
        vflag = True
        for v in valid:
            if v not in single_passport:
                vflag = False

        if vflag is True:
            valid_count += 1
        else:
            invalid_count += 1

    print('Valid', valid_count)
    print('Invalid', invalid_count)


if __name__ == '__main__':
    desc = 'Advent 4a'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
