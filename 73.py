class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        position = []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    position.append([i, j])
        if not position:
            return
        else:
            for pos in position:
                x, y = pos[0], pos[1]
                matrix[x] = [0]*n
                for col in range(m):
                    matrix[col][y] = 0