class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix)
        m = len(matrix[0])

        subM = len(matrix)//2
        subN = len(matrix[0])//2 + len(matrix[0])%2

        for i in range(subM):
            for j in range(subN):
                cur = matrix[i][j]
                nI, nJ = j, n-i-1
                backup = matrix[nI][nJ]
                matrix[nI][nJ] = cur

                # print(matrix)

                cur = backup
                nI, nJ = nJ,n- nI-1
                backup = matrix[nI][nJ]
                matrix[nI][nJ] = cur
                # print(matrix)
                cur = backup
                nI, nJ = nJ, n - nI - 1 
                backup = matrix[nI][nJ]
                matrix[nI][nJ] = cur
                # print(matrix)
                cur = backup
                nI, nJ = nJ, n-1-nI
                matrix[nI][nJ] = cur