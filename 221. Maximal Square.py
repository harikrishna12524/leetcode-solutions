

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        matrix = [[int(i) for i in row] for row in matrix]
        # for i in range(0,m):
        #     for j in range(0,n):
        #         matrix[i][j] = int(matrix[i][j])

        sol = 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if matrix[i][j] == 0 or i == m-1 or j == n-1:
                    pass
                else:
                    right = matrix[i][j+1]
                    lower = matrix[i+1][j]
                    if right == lower and matrix[i+right][j+right] > 0:
                        matrix[i][j] = right + 1
                    else:
                        matrix[i][j] = min(right, lower)
                        if(right != lower):
                            matrix[i][j] += 1

                sol = max(matrix[i][j], sol)

        return sol**2
