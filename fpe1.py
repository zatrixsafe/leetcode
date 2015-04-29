class Sloution:
    def f(self, num):
        left = 0
        right = len(num) - 1
        while left < right:
            mid = (left + right) / 2
            if num[mid] < num[mid+1]:
                left = mid + 1
            else: right = mid
        return left

s = Sloution()
num = [1]
print s.f(num)
num = [1,2,3]
print s.f(num)
num = [1,2]
print s.f(num)
num = [3,2,1]
print s.f(num)
num = [1,2,1]
print s.f(num)
