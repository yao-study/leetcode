#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        retval = strs[0]
        retval_len = len(retval)
        length = len(strs)
        for i in range(1, length):
            each = strs[i]
            each_len = len(each)
            if each_len == 0:
                return ''
            n = 0
            while n < min(retval_len, each_len):
                if retval[n] == each[n]:
                    n += 1
                else:
                    break
            retval = each[0:n]
            retval_len = n

        return retval


s = Solution()
print s.longestCommonPrefix(['yaoi', 'yaoite', 'yaoijj'])
