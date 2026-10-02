class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        # Transpose
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse every row
        for row in matrix:
            row.reverse()