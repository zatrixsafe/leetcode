class Solution:
    def f(self, n):
        s = bin(n)
        print s
        cnt = 0
        for i in s:
            if i == '1':
                cnt += 1
        return cnt

s = Solution()
print s.f(100)
print s.f()
