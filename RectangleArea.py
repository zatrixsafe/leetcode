#!/usr/bin/env python
# File Name: RectangleArea.py
class Solution:
    def f(self, A, B, C, D, E, F, G, H):
        A1 = max(A, E)
        B1 = max(B, F)
        C1 = min(C, G)
        D1 = min(D, H)
        res = self.cals(A, B, C, D) + self.cals(E, F, G, H)
        if C1 <= A1 or D1 <= B1:
            return res
        else: 
            return res - self.cals(A1, B1, C1, D1)

    def cals(self, A, B, C, D):
        return (C - A) * (D - B)

s = Solution()
print s.f(-3, 0, 3, 4, 0, -1, 9, 2)
