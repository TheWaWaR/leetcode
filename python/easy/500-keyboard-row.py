#!/usr/bin/env python
#coding: utf-8


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = 'qwertyuiopQWERTYUIOP'
        row2 = 'asdfghjklASDFGHJKL'
        row3 = 'zxcvbnmZXCVBNM'

        results = []
        for word in words:
            num = None
            for c in word:
                if c in row1:
                    n = 1
                elif c in row2:
                    n = 2
                elif c in row3:
                    n = 3

                if num is None:
                    num = n
                elif num != n:
                    num = None
                    break

            if num is not None:
                results.append(word)

        return results


def main():
    cases = [
        (["Hello", "Alaska", "Dad", "Peace"], ["Alaska", "Dad"])
    ]
    for inputs, outputs in cases:
        results = Solution().findWords(inputs)
        print 'Results', results
        assert results == outputs

if __name__ == '__main__':
    main()
