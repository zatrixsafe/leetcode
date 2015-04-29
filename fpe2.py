class Solution:
    def re(self, le, ri, n, num):
        mid = (le + ri) / 2
        if mid == 0 and num[mid] > num[1]:
            return mid
        elif mid == 0:
            return self.re(mid+1, ri, n, num)
        elif mid == n - 1 and num[mid] > num[n - 2]:
            return mid
        elif num[mid] > num[mid - 1] and num[mid] > num[mid + 1]:
            return mid
        elif num[mid] < num[mid - 1]:
            return self.re(le, mid-1, n, num)
        else: return self.re(mid+1, ri, n, num)
        
    def f(self, num):
        if len(num) == 1:
            return 0
        return self.re(0,len(num) - 1,len(num), num)

s = Solution()
num = [1,2,3,4,5,6]
print s.f(num)
num = [1]
print s.f(num)
num = [3,2,1]
print s.f(num)
num = [1,2,1]
print s.f(num)
num = [1,2]
print s.f(num)
num = [1,2,3]
print s.f(num)
