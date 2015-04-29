class Slution:
    def f(self, n):
        cnt = n / 5
        while n / 5 >= 5:
            n /= 5
            cnt += n / 5
        return cnt
s = Slution()
print s.f(50)
print s.f(0)
print s.f(30)
print s.f(10)
