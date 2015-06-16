#!/usr/bin/env python
# File Name: reverseBit.py

class Solution:
    def reverseBits(self, n):
        st = bin(n)
        s = '0' * (30-len(st))
        st = st[::-1] + s
        return int(st, 2)
s = Solution()
print s.reverseBits(1)
