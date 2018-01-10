#!/usr/bin/env python
#coding: utf-8

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = []
        def generate(s, left, right):
            if left == right:
                if left == n:
                    results.append(s)
                else:
                    generate(s+'(', left+1, right)
            else:
                if left + 1 <= n:
                    generate(s+'(', left+1, right)
                if left >= right + 1:
                    generate(s+')', left, right+1)
        generate('', 0, 0)
        return results


def main():
    from pprint import pprint
    pprint(Solution().generateParenthesis(3))
    pprint(Solution().generateParenthesis(6))


if __name__ == '__main__':
    main()
