"""
Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.
Return the number of negative numbers in grid.

Input: grid = [[4,3,2,-1], [3,2,1,-1], [1,1,-1,-2], [-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
"""

def countNegatives(doubleArray):
    output = 0
    for row in range(len(doubleArray)):
        for column in range(len(doubleArray[row])):
            # print(doubleArray[row][column], end='')  # 432-1321-111-1-2-1-1-2-3
            if doubleArray[row][column] < 0:
                output += 1
    print(f'There are {output} negative numbers in the matrix.')

# array[0][2]   -->   array[2][3] .... etc


countNegatives([[4,3,2,-1], [3,2,1,-1], [1,1,-1,-2], [-1,-1,-2,-3]])