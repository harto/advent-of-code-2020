with open('inputs/18') as f:
    source = f.readlines()

import re

def parse_line(s):
    stack = []
    expr = []
    for c in s:
        if c == '(':
            stack.append(expr)
            expr = []
        elif c == ')':
            stack[-1].append(expr)
            expr = stack.pop()
        elif re.match(r'\d', c):
            expr.append(int(c))
        elif c in ('*', '+'):
            expr.append(c)
    return expr

def eval_expr(expr):
    if isinstance(expr, int):
        return expr

    while len(expr) > 1:
        # part 1
        # lhs, op, rhs = expr[:3]
        # f = int.__add__ if op == '+' else int.__mul__
        # v = f(eval_expr(lhs), eval_expr(rhs))
        # expr = [v] + expr[3:]

        # part 2: find & eval addition first
        i = expr.index('+') if '+' in expr else 1
        lhs, op, rhs = expr[i-1:i+2]
        f = int.__add__ if op == '+' else int.__mul__
        v = f(eval_expr(lhs), eval_expr(rhs))
        expr = expr[:i-1] + [v] + expr[i+2:]

    return expr[0]

print(sum(eval_expr(parse_line(line)) for line in source))
