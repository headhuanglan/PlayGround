#https://leetcode.com/problems/set-matrix-zeroes/description/
class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
#         rset=set()
#         cset=set()
        
#         nr=len(matrix)
#         nc=len(matrix[0])
        
#         for r in range(nr):
#             for c in range(nc):
#                 if matrix[r][c]==0:
#                     rset.add(r)
#                     cset.add(c)
                    
#         for r in range(nr):
#             for c in range(nc):
#                 if r in rset:
#                     matrix[r][c]=0
#                 if c in cset:
#                     matrix[r][c]=0

        col0, rows, cols = 1, len(matrix), len(matrix[0])

        for i in range(0, rows):
            if matrix[i][0] == 0:
                col0 = 0
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(rows-1, -1, -1):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0 == 0:
                matrix[i][0] = 0
      
