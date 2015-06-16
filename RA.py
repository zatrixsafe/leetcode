#!/usr/bin/env python
# File Name: RA.py

class Solution:

    def f(self,A, B, C, D, E, F,G, H):
        liA = self.getRectangle(A, B, C, D) 
        liB = self.getRectangle(E, F, G, H) 
        for p,q in liA:

    def getRectangle(A, B, C, D):
        return [(A, D), (A, B), (C, B), (C, D)]
