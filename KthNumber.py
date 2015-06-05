#!/usr/bin/env python
# File Name: KthNumber.py

class Solution:
    def f(self, nums, k):
        ans = qsort(nums, 0, len(nums), k)

    def qsort(self, nums, beg, end, k):
        q = sf(self, nums, beg, end) 
        if k == q:
            return nums[beg+q] 
        elif k > q:
            qsort(self, nums, q+1, end, k-q)
        else:
            qsort(self, nums, beg, q, k)

    def sf(self, nums, k, beg, end):
        prid = beg
        for i in range(beg+1,end):
            
