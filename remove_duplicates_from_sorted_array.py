#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if not length:
            return 0
        i = 0
        j = 1
        while j < length:
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1
