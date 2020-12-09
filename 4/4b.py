#!/usr/bin/env python

import argparse
import sys
import re


def validate(single_passport):
    """Validate passport vals"""
    valid = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    ecl_valid = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    vflag = True
    for v in valid:
        if v not in single_passport:
            vflag = False

    if vflag:
        if not ((int(single_passport['byr']) <= 2002) and (int(single_passport['byr']) >= 1920)):
            vflag = False
        if not ((int(single_passport['iyr']) <= 2020) and (int(single_passport['iyr']) >= 2010)):
            vflag = False
        if not ((int(single_passport['eyr']) <= 2030) and (int(single_passport['eyr']) >= 2020)):
            vflag = False

        hgt_re = re.match('(\d+)(\w+)', single_passport['hgt'])

        if hgt_re is None:
            vflag = False
        else:
            hgt_val = int(hgt_re.group(1))
            hgt_units = hgt_re.group(2)

            if hgt_units == 'in':
                if not ((hgt_val <= 76) and (hgt_val >= 59)):
                    vflag = False
            elif hgt_units == 'cm':
                if not ((hgt_val <= 193) and (hgt_val >= 150)):
                    vflag = False
            else:
                vflag = False

        hcl_re = re.match('#[0-9a-f]{6}', single_passport['hcl'])

        if hcl_re is None:
            vflag = False

        if single_passport['ecl'] not in ecl_valid:
            vflag = False

        pass_re = re.match('^(\d{9})$', single_passport['pid'])

        if pass_re is None:
            vflag = False
        if len(single_passport['pid']) != 9:
            vflag = False

    return vflag


def main(args):
    """
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    """

    passports = list()
    single_passport = dict()
    valid_count = 0
    invalid_count = 0

    with open(args.input, 'r') as fh:
        for line in fh:
            line = line.rstrip()
            if line == '':
                passports.append(single_passport)
                vflag = validate(single_passport)

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

        # Handle last entry due to no newline at EOF
        vflag = validate(single_passport)

        if vflag is True:
            valid_count += 1
        else:
            invalid_count += 1

    print('Valid', valid_count)
    print('Invalid', invalid_count)


if __name__ == '__main__':
    desc = 'Advent 4b'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
