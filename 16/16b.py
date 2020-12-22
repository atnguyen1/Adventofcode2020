#!/usr/bin/env python3

import argparse
import numpy as np
import sys

def elements_within(elements, r1, r2, r3, r4):
    # Return True if all elements e are r1 <= e <= r2 else false
    for e in elements:
        if not (((r1 <= e) and (e <= r2)) or ((r3 <= e) and (e <= r4))):
            return False
    return True


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
        ovals = oval.split('\n')

        other_tickets = list()

        for o in ovals:
            other_tickets.append([int(y) for y in o.split(',')])

        error_vals = list()
        valid_tickets = list()

        for ot in other_tickets:
            valid = True

            for entry in ot:
                rule_pass = list()
                for r in rules:
                    rl = rules[r]
                    if ((rl[0] <= entry) and (entry <= rl[1])) or ((rl[2] <= entry) and (entry <= rl[3])):
                        rule_pass.append(True)
                    else:
                        rule_pass.append(False)
                
                if True not in rule_pass:
                    error_vals.append(entry)
                    valid = False
            if valid:
                valid_tickets.append(ot)

        # print(sum(error_vals))
        ticket_order = dict()

        a = np.array(valid_tickets, dtype='object')
        used = list()
        for col in range(len(valid_tickets[0])):
            values = list(a[:, col])

            for r in rules:
                rl = rules[r]
                if elements_within(values, rl[0], rl[1], rl[2], rl[3]):
                    if col not in ticket_order:
                        ticket_order[col] = [r]
                    else:
                        ticket_order[col].append(r)

        filt_ticket_order = list()

        solved = list()
        solved_text = set()

        while len(solved) != len(ticket_order.keys()):
            for t in ticket_order.keys():
                matching = set(ticket_order[t])
                matching = matching.difference(solved_text)

                if len(matching) == 1:
                    solved.append((t, list(matching)[0]))
                    solved_text.update(ticket_order[t])
                    # print(solved, solved_text)

        s = sorted(solved, key=lambda x: x[0])
        annotations = [a[1] for a in s]

        translated = dict(zip(annotations, your_ticket))
        print(translated)

        computed = 1
        for key in translated:
            if 'departure' in key:
                computed = computed * translated[key]

        print(computed)


if __name__ == '__main__':
    desc = 'Advent 16b'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
