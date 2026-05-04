class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows=len(matrix)
        cols=rows

        for row in range(rows//2):
            col=row
            while col<cols-1:

                temp1=matrix[col][-1-row+rows]
                matrix[col][-1-row+rows]=matrix[row][col]

                temp2=matrix[-1-row][-1-col]
                matrix[-1-row][-1-col]=temp1

                temp3=matrix[-1-col][row]
                matrix[-1-col][row]=temp2

                matrix[row][col]=temp3

                col+=1
            
            cols-=1
        return matrix
