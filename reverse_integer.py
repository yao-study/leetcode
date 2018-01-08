#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        tmp = str(x)
        sign = ''
        overflow = 2**31 - 1
        if tmp[0] == '-':
            sign = tmp[0]
            tmp = tmp[1:]
        res = tmp[::-1]
        for i in range(len(res)):
            if not res[i] == 0:
                break
        res = res[i:]
        res = int(sign + res)
        if abs(res) > overflow:
            return 0
        else:
            return res
