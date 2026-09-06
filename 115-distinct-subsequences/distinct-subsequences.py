class Solution(object):
    def numDistinct(self, s, t):
        memo = {}

        def solve(i, j):
            if j == len(t):
                return 1

            if i == len(s):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if s[i] == t[j]:
                ans = solve(i + 1, j + 1) + solve(i + 1, j)
            else:
                ans = solve(i + 1, j)

            memo[(i, j)] = ans
            return ans

        return solve(0, 0)