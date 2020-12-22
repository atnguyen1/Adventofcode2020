#!/usr/bin/env python3

import argparse
import math
import sys


class ship:
    def __init__(self, directions):
        self.currentx = 0
        self.currenty = 0
        self.facing = 'E'
        self.directions = directions
        self.direction_index = 0

        self.waypointx = 10
        self.waypointy = 1

    def chugchug(self):
        for d in self.directions:
            direct = d[0]
            value = int(d[1:])

            if direct in ['N', 'E', 'S', 'W']:
                self.move_waypoint(direct, value)
            elif direct in ['L', 'R']:
                self.rotate(direct, value)
            elif direct == 'F':
                self.move(value)
            else:
                print('Invalid command', d, file=sys.stderr)
                sys.exit()

    def chug(self):
        d = self.directions[self.direction_index]
        direct = d[0]
        value = int(d[1:])
        self.direction_index += 1

        if direct in ['N', 'E', 'S', 'W']:
            self.move_waypoint(direct, value)
        elif direct in ['L', 'R']:
            self.rotate(direct, value)
        elif direct == 'F':
            self.move(value)
        else:
            print('Invalid command', d, file=sys.stderr)
            sys.exit()

    def move(self, value):
        # Move times the value in waypoint

        for x in range(value):
            self.currentx += self.waypointx
            self.currenty += self.waypointy

    def move_waypoint(self, direction, value):
        if direction == 'N':
            self.waypointy += value
        elif direction == 'S':
            self.waypointy -= value
        elif direction == 'W':
            self.waypointx -= value
        elif direction == 'E':
            self.waypointx += value
        else:
            print('Invalid Waypoint Move', direction, value, file=sys.stderr)
            sys.exit()

    def rotate(self, direction, value):
        rotation_value = None
        if direction == 'R':
            rotation_value = 360 - value
        else:
            rotation_value = value

        cosx = self.waypointx * round(math.cos(math.radians(rotation_value)))
        sinx = self.waypointy * round(math.sin(math.radians(rotation_value)))

        siny = self.waypointx * round(math.sin(math.radians(rotation_value)))
        cosy = self.waypointy * round(math.cos(math.radians(rotation_value)))

        newx = cosx - sinx
        newy = siny + cosy

        #newx = (self.waypointx * math.cos(math.radians(rotation_value))) - (self.waypointy * math.cos(math.radians(rotation_value)))
        #newy = (self.waypointx * math.sin(math.radians(rotation_value))) + (self.waypointy * math.cos(math.radians(rotation_value)))
        

        self.waypointx = newx
        self.waypointy = newy

    def manahatten(self):
        return abs(self.currentx) + abs(self.currenty)

    def getfacing(self):
        return self.facing

    def getxy(self):
        # X, Y
        return self.currentx, self.currenty

    def getwaypoint(self):
        return self.waypointx, self.waypointy

    def getcurrentdir(self):
        return self.directions[self.direction_index]


def main(args):
    """
    """
    nav = list()
    with open(args.input, 'r') as fh:
        nav = fh.read().split('\n')

    s = ship(nav)
    s.chugchug()
    print(s.manahatten())

    '''
    for x in range(5):
        print(s.getcurrentdir())
        s.chug()
        print('XY', s.getxy())
        print('waypoint', s.getwaypoint())
        print('')
    print(s.manahatten())
    '''


if __name__ == '__main__':
    desc = 'Advent 12a'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
