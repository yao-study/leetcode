#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_len = len(s)
        if s_len == 1:
            return s
        container = [0, '']

        def getPalindrome(index):
            for left, right in [(index, index), (index, index + 1)]:
                while True:
                    if left < 0 or right >= s_len:
                        break
                    if s[left] != s[right]:
                        break
                    else:
                        length = right - left + 1
                        if length > container[0]:
                            container[0], container[1] = length, s[left: right + 1]
                    left -= 1
                    right += 1

        for i in range(s_len - 1):
            getPalindrome(i)
        return container[1]
