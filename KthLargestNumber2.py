#!/usr/bin/env python
# File Name: KthLargestNumber2.py

class Solution:
    def findKthLargest(self, nums, k):
        return self.q(nums, 0, len(nums)-1 ,k-1)

    def q(self, nums, beg, end, k):
        if beg >= end:
            return nums[beg]
        q = self.qSort(nums, beg, end)
        if k == q:
            return nums[q]
        elif k > q:
            return self.q(nums, q+1, end, k)
        else:
            return self.q(nums, beg, q-1, k)

    def qSort(self, nums, beg, end):
        if beg >= end:
            return beg  
        pri = nums[end]
        x = beg - 1
        for i in range(beg, end):
            if nums[i] >= nums[end]:
                x += 1
                nums[i], nums[x] = nums[x], nums[i]
        nums[end], nums[x+1] = nums[x+1], nums[end]
        return x + 1

s = Solution()
nums = [5,2,4,1,3,6,0]
print s.findKthLargest(nums,1)
print s.findKthLargest(nums,2)
print s.findKthLargest(nums,3)
print s.findKthLargest(nums,4)

       

