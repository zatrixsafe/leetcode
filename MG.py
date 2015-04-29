class Solution:
    def maximunGap(self, num):
        if len(num) == 0:
            return 0
        a = sorted(num)
        ans = 0
        for i in range(1,len(num)):
            tmp = abs(a[i] - a[i-1])
            if ans < tmp:
                ans = tmp
        return ans
    
s = Solution()
num = [1,2,2,3,4,5]
print s.maximunGap(num)
            
