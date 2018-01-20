#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        def gen(digits):
            if len(digits) == 1:
                letters = mapping[digits]
                for letter in letters:
                    yield letter
            else:
                first = digits[0]
                other = digits[1:]
                letters = mapping[first]
                for letter in letters:
                    for each in gen(other):
                        yield letter + each

        return list(gen(digits))
