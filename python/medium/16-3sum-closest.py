#!/usr/bin/env python
#coding: utf-8


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums = sorted(nums)
        min_sum = nums[0] + nums[1] + nums[2]
        min_abs = abs(min_sum - target)

        for i in range(len(nums) - 2):
            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                current_sum = nums[i] + nums[lo] + nums[hi]
                if abs(current_sum - target) < min_abs:
                    min_sum = current_sum
                    min_abs = abs(current_sum - target)
                if current_sum > target:
                    hi -= 1
                elif current_sum < target:
                    lo += 1
                else:
                    return target
        return min_sum


def main():
    for nums, target, result in [
            ([-1, 2, 1, -4], 1, 2),
            ([0, 0, 0], 3, 0),
            ([0, 0, 0, 0], 3, 0),
            ([-4, -4, -2, -1, 1], 2, -2)
    ]:
        assert Solution().threeSumClosest(nums, target) == result
        print 'nums={}, target={}, result={}'.format(nums, target, result)
    print 'All tests passed!'


if __name__ == '__main__':
    main()
