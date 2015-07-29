class Solution:
    def searchMatrix(self, matrix, target):
        for i in matrix:
            p = 0
            q = len(i) - 1
            while p <= q:
                mid = (p + q) / 2
                if target == i[mid]:
                    return True
                elif target > i[mid]:
                    p = mid + 1
                else:
                    q = mid - 1
        return False 
s = Solution()
le = [1, 2, 3, 4, 5]
lr = [6, 7, 8, 9, 10]
matrix =[]
matrix.append(le)
matrix.append(lr)
target = 5
print s.searchMatrix(matrix, target)
