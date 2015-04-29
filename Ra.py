class Solution:
    def f(self, nums, k):
        lst = nums[-k : ]
        lst2 = nums[0 : len(nums)-k]
        lst = lst + lst2
        return lst

s = Solution()
nums = [1,2]
print s.f(nums,1)
