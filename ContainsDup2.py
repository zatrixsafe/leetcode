#!/usr/bin/env python
# File Name: ContainsDup2.py

class Solution:
    def f(self, nums, k):
        dit = {}
        ans = 0
        for i, num in enumerate(nums):
            dit[i] = num
        dit = sorted(dit.items(), key = lambda d:d[1])
        l = list(dit)        
        for i in range(1, len(l)):
            if l[i][1] == l[i-1][1]:
                if abs(l[i][0] - l[i-1][0]) <= k:
                    ans += 1
        if ans == 1:
            return True;
        return False;

s = Solution()
nums = [10,12,3,4,5,6]
print s.f(nums, 10)  
