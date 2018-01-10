#!/usr/bin/python
# coding: utf-8


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        digits = '0123456789'
        op_dict = {
            '+': lambda a, b: a+b,
            '-': lambda a, b: a-b,
            '*': lambda a, b: a*b,
            '/': lambda a, b: a/b,
        }

        def parse(i, exp, is_number=False):
            ast = []
            while i < len(exp):
                c = exp[i]
                if c == ' ':
                    pass
                elif c == '(':
                    inner_ast, i = parse(i+1, exp)
                    ast.append(inner_ast)
                elif c == ')':
                    break
                elif c in '+-':
                    ast.append(c)
                elif c in '*/':
                    prev_node = ast.pop()
                    while i < len(exp) and exp[i] == ' ':
                        i += 1
                    if exp[i] == '(':
                        next_node, i = parse(i+1, exp)
                    else:
                        next_node, i = parse(i+1, exp, True)
                    ast.append([prev_node, c, next_node])
                else:
                    number = c
                    while len(exp) > i+1 and exp[i+1] in digits:
                        i += 1
                        number += exp[i]
                    if is_number:
                        return int(number), i
                    ast.append(int(number))
                i += 1
            return ast, i

        ast, _ = parse(0, s)
        # print ast

        def calc(ast):
            if len(ast) == 1:
                return ast[0] if isinstance(ast[0], int) else calc(ast[0])

            value = None
            i = 0
            while i < len(ast):
                node = ast[i]
                if isinstance(node, basestring):
                    if node in op_dict:
                        i += 1
                        next_node = ast[i]
                        next_value = (
                            next_node if isinstance(next_node, int)
                            else calc(next_node)
                        )
                        value = op_dict[node](value, next_value)
                    else:
                        raise ValueError('Invalid node: {}'.format(node))
                elif isinstance(node, int):
                    value = node
                else:
                    value = calc(node)
                i += 1
            return value

        return calc(ast)


if __name__ == '__main__':
    for expr in [
            "(1+(4+5*2/3)-3)+(6+8)",
            "(1+(4+5+2)-3)+(14)",
            "1 + 1",
            "3+2*2",
            " 3/2 ",
            " 3+5 / 2 ",
    ]:
        expect = eval(expr)
        print 'Expr: <{}>'.format(expr)
        rv = Solution().calculate(expr)
        print 'Result={}, Expect={}'.format(rv, expect)
        assert rv == expect
