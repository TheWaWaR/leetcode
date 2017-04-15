#!/usr/bin/env python
#coding: utf-8


class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """

        row_len = len(board)
        col_len = len(board[0])

        def click_it(x, y, mut=False):
            target = board[x][y]
            if target not in ['M', 'E']:
                # 1~8, B, X
                return
            elif target == 'M':
                if mut:
                    board[x][y] = 'X'
                return
            elif target == 'E':
                count = 0
                adjacents = []
                for i in (-1, 0, 1):
                    xi = x + i
                    if 0 <= xi < row_len:
                        for j in (-1, 0, 1):
                            if i == 0 and j == 0:
                                continue
                            yj = y + j
                            if 0 <= yj < col_len:
                                adjacents.append((xi, yj))
                                if board[xi][yj] == 'M':
                                    count += 1
                if count > 0:
                    board[x][y] = str(count)
                else:
                    board[x][y] = 'B'
                    for xi, yj in adjacents:
                        click_it(xi, yj)

        click_it(click[0], click[1], mut=True)
        return board


def main():
    for board, click, result in [
            (
                [['E', 'E', 'E', 'E', 'E'],
                 ['E', 'E', 'M', 'E', 'E'],
                 ['E', 'E', 'E', 'E', 'E'],
                 ['E', 'E', 'E', 'E', 'E']],
                [3,0],
                [['B', '1', 'E', '1', 'B'],
                 ['B', '1', 'M', '1', 'B'],
                 ['B', '1', '1', '1', 'B'],
                 ['B', 'B', 'B', 'B', 'B']]
            ),
            (
                [['B', '1', 'E', '1', 'B'],
                 ['B', '1', 'M', '1', 'B'],
                 ['B', '1', '1', '1', 'B'],
                 ['B', 'B', 'B', 'B', 'B']],
                [1, 2],
                [['B', '1', 'E', '1', 'B'],
                 ['B', '1', 'X', '1', 'B'],
                 ['B', '1', '1', '1', 'B'],
                 ['B', 'B', 'B', 'B', 'B']]
            ),
    ]:
        rv = Solution().updateBoard(board, click)
        print 'Result: {}'.format(rv)
        for x in range(len(rv)):
            for y in range(len(rv[0])):
                assert rv[x][y] == result[x][y]

    print 'All OK'

if __name__ == '__main__':
    main()
