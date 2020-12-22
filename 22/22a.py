#!/usr/bin/env python3

import argparse
import re
from collections import defaultdict, deque
import sys


class Combat():
    def __init__(self, one, two):
        self.player1 = deque(one)
        self.player2 = deque(two)
        self.round = 1

    def trick(self):

        card_one = self.player1.popleft()
        card_two = self.player2.popleft()

        # print(card_one, card_two)

        if card_one > card_two:
            self.player1.append(card_one)
            self.player1.append(card_two)
        elif card_two > card_one:
            self.player2.append(card_two)
            self.player2.append(card_one)
        else:
            print('Error State not >', card_one, card_two)
            sys.exit()

    def complete(self):
        while self.player1 != deque() and self.player2 != deque():
            self.trick()

    def compute_score(self):
        if len(self.player1) > 0:
            winner = self.player1
        else:
            winner = self.player2

        score_multiplier = [x for x in range(1, len(winner) + 1)]
        score_multiplier = score_multiplier[::-1]
        print(score_multiplier)
        print(winner)

        score = 0
        for z, s in enumerate(winner):
            score += s * score_multiplier[z]

        print(score)

    def print_state(self):
        print(self.player1)
        print(self.player2)

def main(args):
    """
    """
    with open(args.input, 'r') as fh:
        data = fh.read().split('\n\n')

        player1 = data[0].split('\n')[1:]
        player1 = [int(x) for x in player1]

        player2 = data[1].split('\n')[1:]
        player2 = [int(x) for x in player2]

        print(player1)
        print(player2)

        game = Combat(player1, player2)
        # game.trick()
        # game.print_state()
        # game.trick()
        # game.print_state()
        game.complete()
        game.print_state()
        game.compute_score()

if __name__ == '__main__':
    desc = 'Advent 22a'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
