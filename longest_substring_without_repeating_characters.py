#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        filter_dict = {}
        start = 0
        max_length = 0
        count = 0
        at_end = False
        while not at_end:
            for idx, char in enumerate(s[start:]):
                idx = start + idx
                if idx == length - 1:
                    at_end = True
                if char not in filter_dict:
                    filter_dict[char] = idx
                    count += 1
                else:
                    pos = filter_dict[char]
                    start = pos + 1
                    filter_dict = {}
                    break
            if count > max_length:
                max_length = count
            count = 0
        return max_length


s = Solution()
print s.lengthOfLongestSubstring('abcabcbb')
