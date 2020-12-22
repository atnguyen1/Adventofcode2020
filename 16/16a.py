#!/usr/bin/env python3

import argparse
import re
import sys


def main(args):
    """
    """
    with open(args.input, 'r') as fh:
        # Split into 3rds
        data = fh.read().split('\n\n')
        rules_unparsed = data[0]
        ticket_info_unparsed = data[1]
        other_ticket_unparsed = data[2]

        # Parse Rules
        rules = dict()
        rules_iter = rules_unparsed.split('\n')

        for r in rules_iter:
            key, val = r.split(':')
            val = val.lstrip()
            vala, valb = val.split(' or ')
            val1, val2 = vala.split('-')
            val3, val4 = valb.split('-')
            rules[key] = [int(val1), int(val2), int(val3), int(val4)]

        # Your Ticket
        tkey, tval = ticket_info_unparsed.split(':')
        tval = tval.lstrip().rstrip()

        your_ticket = [int(x) for x in tval.split(',')]

        # Other's Tickets

        okey, oval = other_ticket_unparsed.split(':')
        oval = oval.rstrip().lstrip()
        oval = oval.replace('\n', ',')

        other_tickets = [int(y) for y in oval.split(',')]

        error_vals = list()

        for entry in other_tickets:
            rule_pass = list()
            for r in rules:
                rl = rules[r]
                if ((rl[0] <= entry) and (entry <= rl[1])) or ((rl[2] <= entry) and (entry <= rl[3])):
                    rule_pass.append(True)
                else:
                    rule_pass.append(False)
            
            if True not in rule_pass:
                error_vals.append(entry)


        print(error_vals)
        print(sum(error_vals))


        '''
        for d in data:
            try:
                key, val = d.split(':')
                info[key] = val
            except:
                print(d)
                sys.exit()
        '''


if __name__ == '__main__':
    desc = 'Advent 16a'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
