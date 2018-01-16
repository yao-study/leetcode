#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        _len = length
        maxarea = 0
        max_height = 0
        while _len >= 1:
            for i in xrange(0, length - _len):
                j = i + _len
                i_height = height[i]
                j_height = height[j]
                the_min = min(i_height, j_height)
                if the_min <= max_height:
                    continue
                else:
                    max_height = the_min
                area = _len * the_min
                if area > maxarea:
                    maxarea = area

            _len -= 1
        return maxarea


s = Solution()
print s.maxArea([1, 3, 2, 2])
