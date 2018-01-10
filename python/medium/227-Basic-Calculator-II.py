#!/usr/bin/env python
# coding: utf-8


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        tokens = []
        ops = '+-*/'
        number = ''
        op = None
        for c in s:
            is_number = False
            if c == ' ':
                continue
            elif c in ops:
                op = c
            else:
                is_number = True
                number += c

            if not is_number:
                tokens.append(int(number))
                number = ''
            if op:
                tokens.append(op)
                op = None
        if number:
            tokens.append(int(number))

        op_dict = {
            '+': lambda a, b: a+b,
            '-': lambda a, b: a-b,
            '*': lambda a, b: a*b,
            '/': lambda a, b: a/b,
        }
        for level_ops in ['*/', '+-']:
            new_tokens = []
            i = 0
            while i < len(tokens):
                token = tokens[i]
                if isinstance(token, basestring) and token in level_ops:
                    i += 1
                    last_token = new_tokens.pop()
                    next_token = tokens[i]
                    new_tokens.append(op_dict[token](last_token, next_token))
                else:
                    new_tokens.append(token)
                i += 1
            tokens = new_tokens
        return tokens[0]


if __name__ == '__main__':
    for expr, expect in [
            ("1 + 1", 2),
            ("3+2*2", 7),
            (" 3/2 ", 1),
            (" 3+5 / 2 ", 5)]:
        print 'Expr: <{}>'.format(expr)
        rv = Solution().calculate(expr)
        print 'Result={}, Expect={}'.format(rv, expect)
        assert rv == expect
