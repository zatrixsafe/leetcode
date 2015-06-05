#!/usr/bin/env python
# File Name: ContainsDup1.py


class Solution:
    def f(self, nums):
        l = sorted(nums)
        for i in range(1, len(l)):
            if l[i] == l[i-1]:
                return True
        return False
