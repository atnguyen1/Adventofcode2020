#!/usr/bin/env python3

import argparse
import re
from collections import defaultdict, deque
import sys

# Memoize deck states and who wins
GLOBAL_STATES = dict()
GLOBAL_GAME_COUNT = 1

class Combat():
    def __init__(self, one, two, game_count):
        self.player1 = deque(one)
        self.player2 = deque(two)
        self.round = 1
        # self.game_count = game_count
        self.current_game_id = game_count

        self.round_record = list()

        #! print('=== Game ' + str(game_count) + ' ===')
        #! print('')

    def trick(self):
        global GLOBAL_GAME_COUNT
        global GLOBAL_STATES
        # Check infinite case
        start_record_1 = ''.join([str(x) for x in self.player1])
        start_record_2 = ''.join([str(y) for y in self.player2])
        record = start_record_1 + '-' + start_record_2
        if record in self.round_record:
            # We've played this state before
            #! print('-- Round ' + str(self.round) + ' (Game ' + str(self.current_game_id) + ') --')
            #! print('Player 1\'s deck:', self.player1)
            #! print('Player 2\'s deck:', self.player2)
            #! print('Previous State Player 1 Wins')
            return 0
        else:
            self.round_record.append(record)

        #! print('-- Round ' + str(self.round) + ' (Game ' + str(self.current_game_id) + ') --')
        #! print('Player 1\'s deck:', self.player1)
        #! print('Player 2\'s deck:', self.player2)
        card_one = self.player1.popleft()
        card_two = self.player2.popleft()
        #! print('Player 1 plays', card_one)
        #! print('Player 2 plays', card_two)


        if (len(self.player1) >= card_one) and (len(self.player2) >= card_two):
            # Recurse

            #! print('Playing a sub-game to determine the winner...')
            #! print('')
            new_1_deck = [x for z, x in enumerate(self.player1) if z < card_one]
            new_2_deck = [y for w, y in enumerate(self.player2) if w < card_two]
            GLOBAL_GAME_COUNT += 1

            # memoize string of deck + winner
            subgame1_str = [str(x) for x in new_1_deck]
            subgame1_str = ''.join(subgame1_str)
            subgame2_str = [str(y) for y in new_2_deck]
            subgame2_str = ''.join(subgame2_str)
            subgame_record = subgame1_str + '-' + subgame2_str

            if subgame_record in GLOBAL_STATES:
                ng_winner = GLOBAL_STATES[subgame_record]
            else:
                ng = Combat(new_1_deck, new_2_deck, GLOBAL_GAME_COUNT)
                ng_winner = ng.complete()
                GLOBAL_STATES[subgame_record] = ng_winner
            #! print('...anyway, back to game ' + str(self.current_game_id) + '.')

            if ng_winner == 1:
                # Player one wins trick
                #! print('Player 1 Wins round ' + str(self.round) + ' of game ' + str(self.current_game_id))
                #! print('')
                self.player1.append(card_one)
                self.player1.append(card_two)
            elif ng_winner == 2:
                #! print('Player 2 Wins round ' + str(self.round) + ' of game ' + str(self.current_game_id))
                #! print('')
                self.player2.append(card_two)
                self.player2.append(card_one)
        else:
            if card_one > card_two:
                #! print('Player 1 Wins round ' + str(self.round) + ' of game ' + str(self.current_game_id))
                #! print('')
                self.player1.append(card_one)
                self.player1.append(card_two)
            elif card_two > card_one:
                #! print('Player 2 Wins round ' + str(self.round) + ' of game ' + str(self.current_game_id))
                #! print('')
                self.player2.append(card_two)
                self.player2.append(card_one)
            else:
                print('Error State not >', card_one, card_two)
                sys.exit()

        self.round += 1
        return 1         # Use return states to stop infinte recursion


    def complete(self):
        while self.player1 != deque() and self.player2 != deque():
            success = self.trick()
            if success == 0:
                return 1       # If we hit previous round state, player 1 wins

        # Return Winner
        if self.player1 == deque():
            #! print('The winner of game ' + str(self.current_game_id) + ' is player ' + str(2) + '!')
            #! print('')
            return 2
        else:
            #! print('The winner of game ' + str(self.current_game_id) + ' is player ' + str(1) + '!')
            #! print('')
            return 1

    def compute_score(self):
        if len(self.player1) > 0:
            winner = self.player1
        else:
            winner = self.player2

        score_multiplier = [x for x in range(1, len(winner) + 1)]
        score_multiplier = score_multiplier[::-1]
        #print(score_multiplier)
        #print(winner)

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

        # print('Starting Player1:', player1)
        # print('Starting Player2:', player2)

        game = Combat(player1, player2, 1)
        winner = game.complete()
        game.compute_score()


if __name__ == '__main__':
    desc = 'Advent 22b'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
