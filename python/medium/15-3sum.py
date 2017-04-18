#!/usr/bin/env python
#coding: utf-8


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        results.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        return [list(result) for result in results]


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def binary_search(lst, v):
            if not lst:
                return False
            mid = len(lst) / 2
            if v > lst[mid]:
                return binary_search(lst[mid+1:], v)
            elif v < lst[mid]:
                return binary_search(lst[:mid], v)
            else:
                return True

        pos_nums = sorted([n for n in nums if n > 0])
        neg_nums = sorted([n for n in nums if n < 0])
        zero_len = len([n for n in nums if n == 0])

        results = []
        def collect(one_nums, two_nums):
            for one_n in set(one_nums):
                prev = (None, None)
                for i in range(len(two_nums)):
                    two_n1 = two_nums[i]
                    two_n2 = - one_n - two_n1
                    if (two_n1, two_n2) != prev and binary_search(two_nums[i+1:], two_n2):
                        results.append(sorted([one_n, two_n1, two_n2]))
                        prev = (two_n1, two_n2)

        collect(pos_nums, neg_nums)
        collect(neg_nums, pos_nums)
        if zero_len >= 3:
            results.append([0, 0, 0])
        if zero_len >= 1:
            for pos_n in set(pos_nums):
                if binary_search(neg_nums, -pos_n):
                    results.append([-pos_n, 0, pos_n])

        return results


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums = sorted(nums)
        results = []
        for i in range(len(nums)-2):
            if nums[i] == nums[i+1] == nums[i+2]:
                if nums[i] == 0:
                    results.append([0, 0, 0])
                    break
                continue
            lo = i + 1
            hi = len(nums) - 1
            total = 0 - nums[i]
            while lo < hi:
                if (nums[i] != nums[i+1] or nums[i] == nums[lo]) and nums[lo] + nums[hi] == total:
                    results.append([nums[i], nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == nums[lo+1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi-1]:
                        hi -= 1
                    lo += 1
                    hi -= 1
                elif nums[lo] + nums[hi] < total:
                    lo += 1
                else:
                    hi -= 1
        return results


def main():
    for s, result in [
            (
                [-1, 0, 1, 2, -1, -4],  # [-4, -1, -1, 0, 1, 2]
                [[-1, 0, 1], [-1, -1, 2]]),
            (
                [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0],
                []
            ),
            (
                [0, 0, 0, 0, 0],
                []
            )
    ]:
        print Solution().threeSum(s)


if __name__ == '__main__':
    main()
