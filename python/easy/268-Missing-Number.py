#!/usr/bin/env python
# coding: utf-8


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i, n in enumerate(nums):
            if i != n:
                return i
        return len(nums)
