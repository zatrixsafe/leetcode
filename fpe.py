class Slution:
    def f(self, num):
        if len(num) == 1:
            return 0
        for i in range(len(num)):
            if i == 0:
                if num[i] > num[i+1]:
                    return i
            elif i == len(num) - 1:
                if num[i] > num[i-1]:
                    return i
            elif num[i] > num[i-1] and num[i] > num[i+1]:
                return i
s = Slution()
lst = [1,2]
lst1 = [100]
lst2 = [1,2,1]
print s.f(lst1)
print s.f(lst)
print s.f(lst2)
