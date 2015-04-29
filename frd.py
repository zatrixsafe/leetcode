class Solution:
    def f(self, numerator, denominator):
        st = ''
        nu = numerator
        de = denominator
        if nu < 0 and de < 0:
            nu = -nu
            de = -de
        elif nu < 0:
            nu = -nu
            st += '-'
        elif de < 0:
            de = -de
            if not nu == 0:
                st += '-'
        part = nu % de
        integer = nu / de
        lst = []
        num = []
        st += str(integer)
        while part % de != 0:
            part *= 10
            for i in range(len(num)):
                if num[i] == part:
                    lst.insert(i,'(')
                    lst.insert(len(lst),')')
                    st = st + '.' + ''.join(lst)
                    return st
            num.append(part)
            lst.append(str(part/de))
            part %= de
        if len(lst) != 0:
            st = st + '.' + ''.join(lst)
        return st
s = Solution()
print s.f(1,17)
print s.f(1,3)
print s.f(1,6)
print s.f(1,333)
print s.f(-50,8)
print s.f(-1,-1)
print s.f(0,-1)
