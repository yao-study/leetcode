#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        i = 0
        last = None
        while i < length - 2:
            k = length - 1
            j = i + 1
            while k > j:
                three_sum = nums[i] + nums[j] + nums[k]
                if three_sum == target:
                    return target
                if last is None:
                    last = three_sum
                elif abs(three_sum - target) <= abs(last - target):
                    last = three_sum
                if three_sum > target:
                    k -= 1
                elif three_sum < target:
                    j += 1
            i += 1
        return last


s = Solution()
print s.threeSumClosest([1, 1, 1, 0], 100)
