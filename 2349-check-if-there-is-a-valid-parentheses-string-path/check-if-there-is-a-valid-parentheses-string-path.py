class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        memo = {}

        if (m + n - 1) % 2 != 0:
            return False

        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        def dfs(i, j, balance):
            if grid[i][j] == '(':
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                return False

            if balance > (m - i) + (n - j) - 1:
                return False

            if i == m - 1 and j == n - 1:
                return balance == 0

            key = (i, j, balance)

            if key in memo:
                return memo[key]

            result = False

            if i + 1 < m:
                result = dfs(i + 1, j, balance)

            if not result and j + 1 < n:
                result = dfs(i, j + 1, balance)

            memo[key] = result
            return result

        return dfs(0, 0, 0)