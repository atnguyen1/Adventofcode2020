#!/usr/bin/env python3

import argparse
from collections import deque
import math
import sys


def get_common_timepoint(bus1, bus2, time, time_offset):
    b1_time = bus1[0]
    b1_offset = bus1[1]

    b2_time = bus2[0]
    b2_offset = bus2[1]

    while True:

        # print(time, time / b1_time, b1_offset)
        # print(time, time / b2_time, b2_offset)

        if (time + b1_offset) % b1_time == 0:
            if (time + b2_offset) % b2_time == 0:
                break

        time += time_offset

    return time

# sdef check(bus_line, offset):


def get_common_timepoint2(buses):
    time = 0
    time_offset = 1

    bus_start = 2
    bus_subset = buses[:bus_start]
    print(buses)
    print(bus_subset)

    while True:

        res = map(lambda x: (time + x[1]) % x[0], bus_subset)
        s = 0   #sum(list(res))
        out = list()
        for r in res:
            s += r
            out.append(r)

        print(time, time_offset, out, s)
        if s == 0:
            # Found common multiple
            if len(bus_subset) == len(buses):
                # Found everything
                break
            else:
                time_offset = math.prod([y[0] for y in bus_subset])
                bus_start += 1
                bus_subset = buses[:bus_start]
                print(bus_subset)
        else:
            time += time_offset

    print(time)
    

def main(args):
    """
    """
    with open(args.input, 'r') as fh:
        earliest_departure = int(fh.readline())
        buses = fh.readline().split(',')

        bus_offsets = list()
        for z, b in enumerate(buses):
            if b == 'x':
                continue
            bus_offsets.append([int(b), int(z)])

        # new_bus = get_common_timepoint2(bus_offsets)
        buses = bus_offsets

        time = 1
        time_offset = 1

        bus_start = 1
        bus_subset = buses[:bus_start]
        print(buses)
        print(bus_subset)

        while True:
            # Computing T + Offset mod BusLine = 0, for enumerating T
            res = map(lambda x: (time + x[1]) % x[0], bus_subset)
            s = 0   # hold sums
            out = list()
            for r in res:
                s += r
                out.append(r)

            print(time, time_offset, out, s)
            if s == 0:
                # Found common multiple
                if len(bus_subset) == len(buses):
                    # Found everything
                    break
                else:
                    # Haven't exhausted list, just common multiples of a few
                    # 
                    time_offset = math.prod([y[0] for y in bus_subset])
                    bus_start += 1
                    bus_subset = buses[:bus_start]
                    print(bus_subset)
            else:
                time += time_offset

        print('Target Time', time)


        '''
        # Slow brute force way
        time = largest + 2
        modulo_pass = True

        while modulo_pass:

            check_vector = list()

            for x in bus_offsets:
                mod = (time + x[1]) % x[0]

                if mod == 0:
                    check_vector.append(True)
                else:
                    check_vector.append(False)

            if False in check_vector:
                time += 1
            else:
                modulo_pass = False

        print(time)
        '''


if __name__ == '__main__':
    desc = 'Advent 13b'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
