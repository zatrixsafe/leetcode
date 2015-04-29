class Solution:
    def f(slef,x):
        k = abs(x)
        ans = 0
        while k > 0:
            tmp = k % 10
            ans = ans + tmp
            ans = ans * 10
            k = k / 10
        ans = ans / 10
        if x < 0:
            ans = - ans
        if ans > 2 ** 31 -1 or ans < -(ans ** 31):
            print 0
            return 0
        else:
            print ans
            return ans
s = Solution()
s.f(2**31)
