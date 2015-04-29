class Slution:
    def f(self, num):
        num -= 1
        base = 26
        st = ''
        while num != -1:
            s = num % base
            st += chr(ord('A') + s)
            num = num / base - 1
        return st[::-1]
s = Slution()
for i in range(700):
    print i,s.f(i)
