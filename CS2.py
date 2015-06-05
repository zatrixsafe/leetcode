#!/usr/bin/env python
# File Name: CS2.py

class Solution:
    lis = []
    def f(self, k, n):
        self.lis = []
        self.sf(k, n,[])
        return self.lis
    def sf(self, k, n, se):
        if len(se) > 0:
            begin = se[-1] + 1
        else:
            begin = 1
        for i in range(begin, 10):
            if n - i == 0 and k == 1:
                se.append(i)
                self.lis.append(list(se))
                se.remove(i)
                return 
            elif n - i > 0 and k > 0:
                se.append(i)
                self.sf(k - 1, n - i, se)
                se.remove(i)
            else:
                return
        return 

s = Solution()
print s.f(9,45)
print s.f(1,1)
