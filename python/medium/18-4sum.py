#!/usr/bin/env python
# coding: utf-8


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def process(start, end, length, total):
            results = []
            for i in range(start, end):
                for j in range(length+1):
                    pass
            return results

        # results = []
        # for i in range(len(nums)-1):
        #     for j in range(length+1):
        #         results.extend(process(i, j, length-j, target))
        return process(0, len(nums), 4, target)


if __name__ == '__main__':
    for nums, target, results in [
            ([1, 0, -1, 0, -2, 2], 0, [
                [-1,  0, 0, 1],
                [-2, -1, 1, 2],
                [-2,  0, 0, 2]
            ])
    ]:
        rv = Solution().fourSum(nums, target)
        print 'Result: {}'.format(rv)
        print 'Expect: {}'.format(results)
        assert sorted(results) == sorted(rv)
