#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {
            '{': '}',
            '[': ']',
            '(': ')',
        }
        tmp = ''
        for char in s:
            if char in mapping:
                tmp += char
            else:
                if not tmp:
                    return False
                if mapping[tmp[-1]] != char:
                    return False
                tmp = tmp[:-1]
        return len(tmp) == 0
