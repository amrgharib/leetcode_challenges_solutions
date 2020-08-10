class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rot = []

        r, c, f, t = len(grid), len(grid[0]), 0, 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    rot.append([i, j])
                elif grid[i][j] == 1:
                    f += 1

        while len(rot) > 0:
            n = len(rot)

            for x in range(n):
                i, j = rot[0]
                rot.pop(0)

                if i > 0 and grid[i - 1][j] == 1:
                    grid[i - 1][j] = 2
                    f -= 1
                    rot.append([i - 1, j])
                if j > 0 and grid[i][j - 1] == 1:
                    grid[i][j - 1] = 2
                    f -= 1
                    rot.append([i, j - 1])
                if i < r - 1 and grid[i + 1][j] == 1:
                    grid[i + 1][j] = 2
                    f -= 1
                    rot.append([i + 1, j])
                if j < c - 1 and grid[i][j + 1] == 1:
                    grid[i][j + 1] = 2
                    f -= 1
                    rot.append([i, j + 1])

            if len(rot) > 0:
                t += 1

        return t if (f == 0) else -1
