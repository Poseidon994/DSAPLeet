class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def helper_func(matrix:List[List[int]],k:int,m:int,n:int,guess:int)->int:
            row,col=n-1,0
            count=0
            while row>=0 and col<m:
                if matrix[row][col]<=guess:
                    count+=row+1
                    col+=1
                else:
                    row-=1
            return count
        low,high=matrix[0][0],matrix[len(matrix[0])-1][len(matrix)-1]
        res=-1
        while low<=high:
            guess=(low+high)//2
            ans=helper_func(matrix,k,len(matrix[0]),len(matrix),guess)
            if ans<k:
                low=guess+1
            else:
                res=guess
                high=guess-1
        return res