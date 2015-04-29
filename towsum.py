class Solution:
    def twoSum(self, num, target): 
        lst = []
        for i in num:
            lst.append(i)
        i = 0
        j = len(lst) - 1
        lst.sort()
        while i < j:
            if lst[i] + lst[j] > target:
                j = j - 1
            elif lst[i] + lst[j] < target:
                i = i + 1
            else:
                index1 = index2 = 0
                index1 = num.index(lst[i])
                if lst[i] == lst[j]:
                    num.remove(lst[i])
                    index2 = num.index(lst[j]) + 1
                else:
                    index2 = num.index(lst[j])
                if index1 > index2:
                   tmp = index1
                   index1 = index2
                   index2 = tmp
                return (index1 + 1,index2 + 1)
p = Solution()
numbers=[0,4,3,0]
target=0
p.twoSum(numbers, target) 

