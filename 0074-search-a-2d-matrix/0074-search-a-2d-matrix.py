class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low,high=0,len(matrix)*len(matrix[0])-1
        row,col=0,0
        while low<=high:
            guess=(low+high)//2
            row=guess//len(matrix[0])
            col=guess%len(matrix[0])
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                low=guess+1
            else:
                high=guess-1
        return False