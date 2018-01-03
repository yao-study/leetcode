#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a, b, m, n = nums1, nums2, len(nums1), len(nums2)
        if n < m:
            a, b, m, n = b, a, n, m
        if n == 0:
            raise ValueError('invalid lists')

        mini, maxi, = 0, m
        ij_sum = (m + n + 1) / 2
        while True:
            i = (mini + maxi) / 2
            j = ij_sum - i
            print 'i', i
            print 'j', j
            print '--------------------'
            if i < m and a[i] < b[j - 1]:
                mini = i + 1
            elif i > 0 and a[i - 1] > b[j]:
                maxi = i - 1
            else:
                if j == 0:
                    maxleft = a[i - 1]
                elif i == 0:
                    maxleft = b[j - 1]
                else:
                    maxleft = max(a[i - 1], b[j - 1])

                if (m + n) % 2 == 1:
                    return maxleft

                if i == m:
                    minright = b[j]
                elif j == n:
                    minright = a[i]
                else:
                    minright = min(a[i], b[j])
                return (maxleft + minright) / 2.0


s = Solution()
print s.findMedianSortedArrays([], [3, 4])
