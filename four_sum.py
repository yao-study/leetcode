#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        retval = []
        nums.sort()
        a = 0
        length = len(nums)
        while a < length - 3:
            if a > 0 and nums[a - 1] == nums[a]:
                a += 1
                continue
            if nums[a] + nums[a + 1] + nums[a + 2] + nums[a + 3] > target:
                break
            if nums[a] + nums[-3] + nums[-2] + nums[-1] < target:
                a += 1
                continue
            b = a + 1
            while b < length - 2:
                if b > a + 1 and nums[b - 1] == nums[b]:
                    b += 1
                    continue
                c = b + 1
                d = length - 1
                while c < d:
                    if c > b + 1 and nums[c - 1] == nums[c]:
                        c += 1
                        continue
                    if d < length - 1 and nums[d + 1] == nums[d]:
                        d -= 1
                        continue
                    value = nums[a] + nums[b] + nums[c] + nums[d]
                    if value == target:
                        retval.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1
                    elif value > target:
                        d -= 1
                    else:
                        c += 1
                b += 1
            a += 1
        return retval


s = Solution()
print(s.fourSum([1, 2, -1, -2, 8, -8], 0))
