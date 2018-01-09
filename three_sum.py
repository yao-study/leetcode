#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''
        ans = []
        cnt = collections.Counter(nums)
        keys = sorted(cnt.keys())
        keyset = set(keys)
        for i, k in enumerate(keys):
            if k == 0 and cnt[k]>=3:
                ans.append([0,0,0])
            elif k != 0 and cnt[k]>=2 and -2*k in keyset:
                ans.append([k,k,-2*k])
            for k2 in keys[i+1:]:
                k3 = 0-k-k2
                if k3 > k2 and k3 in keyset:
                    ans.append([k,k2,k3])
        return ans
        '''
        ret = []
        nums.sort()
        length = len(nums)
        for i in range(length - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            j = i + 1
            k = length - 1
            while k > j:
                s = nums[i] + nums[j] + nums[k]
                if (s == 0):
                    if (nums[j] > nums[j - 1]) or j == i + 1:
                        ret.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif (s > 0):
                    k -= 1
                else:
                    j += 1
        return ret


s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
