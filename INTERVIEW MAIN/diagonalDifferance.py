"""
Given a square matrix
1   2   3   4   5       0,0                                     0, len(thematrix)-(x-1)
4   5   6   7   8           1,1                             1, len(thematrix)-(x-1)
9   8   9   2   3               2,2                     2, len(thematrix)-(x-1)
5   6   7   8   9                   3,3             3, len(thematrix)-(x-1)
3   6   5   4   8                       4,4     4, len(thematrix)-(x-1)

Calculate the absolute difference between the sum of the diagonals.
EX:     1 + 5 + 9 = 15
        3 + 5 + 9 = 17

        | 15 - 17 | = 2

0,0 + 1,1 + len(thematrix)-1,len(thematrix)-1
0,len(thematrix)-1
"""
# len(matrix) works since it is square
class Solution(object):

    def matrixSums(self, matrixsent):
        print(matrixsent)
        print(f'len = {len(matrixsent)}')
        sum1, sum2 = 0, 0
        for x in range(len(matrixsent)):
            sum1 = sum1 + matrixsent[x][x]
            sum2 = sum2 + matrixsent[x][len(matrixsent)-x-1]
        print(f'\nsum1 - sum2 = {sum1 - sum2}')
        return abs(sum1 - sum2)


theMatrix = ([1, 2, 3], [4, 5, 6], [9, 8, 9])
check = Solution()
print(f'Absolute Difference = {check.matrixSums(theMatrix)}')
