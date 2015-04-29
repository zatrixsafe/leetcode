import string
class Solution:
    def compareVersion(self, version1, version2):
        s1 = version1.split('.')
        s2 = version2.split('.')
        len1 = len(s1)
        len2 = len(s2)
        if len1 > len2:
            length = len1
        else:
            length = len2
        for i in range(length):
            tmp1 = tmp2 = 0
            if i < len1:
                tmp1 = int(s1[i])
            if i < len2:
                tmp2 = int(s2[i])
            
            if tmp1 > tmp2:
                return 1
            elif tmp2 > tmp1:
                return -1
        return 0
s = Solution()
v1 = '01'
v2 = '1'
print s.compareVersion(v1,v2)
