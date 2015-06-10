#!/usr/bin/env python
# File Name: KthNumber.py

class Solution:
    def ff(self,nums,k):
        #print len(nums) + 1 -k 
        return self.f(nums, len(nums)+1-k)
    def f(self, nums, k):
        return self.qsort(nums, 0, len(nums)-1, k-1)
    def qsort(self, nums, beg, end, k):
        q = self.sf(nums, beg, end) 
        if k == q:
            return nums[q] 
        elif k > q:
            return self.qsort(nums, q+1, end, k)
        else:
            return self.qsort(nums, beg, q-1, k)

    def sf(self, nums, beg, end):       
        #print beg,end
        if beg >= end: 
            return end 
        x = nums[end] 
        cnt = beg-1
        for i in range(beg, end):
            if nums[i] <= x:
                cnt += 1
                nums[i], nums[cnt] = nums[cnt], nums[i]
        nums[end], nums[cnt+1] = nums[cnt+1], nums[end]
        #print nums
        return cnt + 1 

s = Solution()
k = [5,2,4,1,3,6,0]
print s.ff(k,2)
