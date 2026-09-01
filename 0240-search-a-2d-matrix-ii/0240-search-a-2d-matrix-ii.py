class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix[0]),len(matrix)
        row,col=n-1,0
        while row>=0 and col<m:
            if matrix[row][col]==target:
                return True
            if matrix[row][col]>target:
                row-=1
            else:
                col+=1
        return False