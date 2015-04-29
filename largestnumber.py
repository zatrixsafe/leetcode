class Solution:
    def cmpare(self, x, y):
        a = x + y
        b = y + x
        return int(b) - int(a)
    def largestNumber(self, num):
        nu = []
        for i in num:
            nu.append(str(i))
        s = sorted(nu, cmp=self.cmpare)
        ans = ''.join(s)
        if ans.startswith('0'):
            ans = '0'
        return ans
s = Solution()
num = [4,2,3,411]
print s.largestNumber(num)
