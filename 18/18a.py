#!/usr/bin/env python3

import argparse
import ast
from collections import deque
# import numpy as np
# import re
# import math
import sys


# np.set_printoptions(threshold=sys.maxsize)


def main(args):
    """
    """
    operators = ['*', '+', '-']

    with open(args.input, 'r') as fh:
        equations = fh.read().split('\n')

        # Test Cases
        # equations = ['A * B + C']
        # equations = ['A * ( B + C )']
        # equations = ['A - B + C']
        # equations = ['A * (B + C * D) + E']
        # equations = ['1 + 2 * 3 + 4 * 5 + 6']
        # equations = ['1 + (2 * 3) + (4 * (5 + 6))']
        # equations = ['2 * 3 + (4 * 5)']
        # equations = ['((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2']

        values = list()

        for e in equations:
            # Tokenize
            e = e.replace(' ', '')
            e = [i for i in e]

            # SHUNTING-YARD
            # convert infix to postfix notation
            # http://mathcenter.oxford.emory.edu/site/cs171/shuntingYardAlgorithm/
            # Hacked so that * and + are same precedence
            postfix = deque()
            operator_stack = deque()

            for z, token in enumerate(e):
                # print(z, token)
                # print(postfix)
                # print(operator_stack)
                if token == '(':
                    operator_stack.append('(')
                    continue
                elif token == ')':
                    # Pop off operator stack till '('
                    t = operator_stack.pop()
                    while t != '(':
                        postfix.append(t)
                        t = operator_stack.pop()
                    continue
                elif token not in operators:
                    postfix.append(token)
                    continue
                elif token in operators:
                    while len(operator_stack) > 0 and operator_stack[-1] != '(':
                        t = operator_stack.pop()
                        postfix.append(t)
                    operator_stack.append(token)

            while len(operator_stack) > 0:
                postfix.append(operator_stack.pop())
            # print(postfix)

            output = deque()

            for p in postfix:
                if p not in operators:
                    output.append(p)
                    continue
                elif p in operators:         # All operators are binary in nature + * -
                    a = output.pop()
                    b = output.pop()
                    expr = a + p + b
                    output.append(str(eval(expr)))

            evaluated = int(output.pop())
            values.append(evaluated)
    print(sum(values))


if __name__ == '__main__':
    desc = 'Advent 18a'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--input', type=str, help='Puzzle Input')

    args = parser.parse_args()

    main(args)
