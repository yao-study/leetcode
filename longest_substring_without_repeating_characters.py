#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        filter_dict = {}
        start = 0
        max_length = 0
        count = 0
        for idx, char in enumerate(s):
            if char not in filter_dict or char in filter_dict and filter_dict[char] < start:
                filter_dict[char] = idx
                count += 1
            else:
                pos = filter_dict[char]
                start = pos + 1
                filter_dict[char] = idx
                if count > max_length:
                    max_length = count
                count = idx - pos
        if count > max_length:
            max_length = count
        return max_length


s = Solution()
print(s.lengthOfLongestSubstring('abcabcdeggbb1234567890'))
