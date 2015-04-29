#!/usr/bin/env python
# File Name: happyNumber.py

class Solution:
    def isHappy(self, n):
        dic = set()
        while not dic.has_key(n):
            dic[n] = 1 
            print n
            lst = []
            sumu = 0
            while(n > 0):
                lst.append(n%10)
                n /= 10
            for i in lst:
                sumu += i**2
            n = sumu
            if n == 1: 
                return True
        return False

s = Solution()
print s.isHappy(11)
