class Slution:
    def f(self, num):
        d = dict()
        n = len(num)
        if n == 1 or n == 2:
            return num[0]
        for i in num:
            if d.has_key(i):
                d[i] += 1
            else:
                d[i] = 1
        for i in d:
            if d[i] > (n / 2):
                return i
lst = [1,1,1,1,1,1,2,333333333,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
s = Slution()
print s.f(lst)
