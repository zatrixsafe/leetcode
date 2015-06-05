#!/usr/bin/env python
# File Name: KthNumber.py

class Solution:
    def f(self, nums, k):
        ans = qsort(nums, 0, len(nums)-1, k)

    def qsort(self, nums, beg, end, k):
        q = sf(self, nums, beg, end) 
        if k == q:
            return nums[beg+q] 
        elif k > q:
            qsort(self, nums, q+1, end, k-q)
        else:
            qsort(self, nums, beg, q, k)

    def sf(self, nums, k, beg, end):
        if beg >= end:
            return
        prid = beg
        #get the number of the prid 
