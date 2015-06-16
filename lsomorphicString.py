#!/usr/bin/env python
# File Name: lsomorphicString.py
import copy
class Solution:
    def isIsomorphic(self, s, t):
        dic = {}
        setbox = set()
        for i in range(len(s)):
            if s[i] in dic:
                if t[i] != dic[s[i]]:
                    return False
            elif t[i] in setbox:
                    return False
            else:
                setbox.add(t[i])
                dic[s[i]] = t[i]
        return True
s = Solution()
print s.isIsomorphic('sss','tta')
print s.isIsomorphic('edd','agg')
print s.isIsomorphic('foo','bar')
print s.isIsomorphic('paper','title')
