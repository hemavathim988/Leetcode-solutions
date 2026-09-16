class Solution:
    def numberOfSets(self, n, k):
        MOD = 10**9 + 7

        # dp[i][j] = number of ways to draw j segments
        # using the first i points
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        # With 0 segments, there is exactly 1 way
        for i in range(n + 1):
            dp[i][0] = 1

        for j in range(1, k + 1):
            prefix = 0

            for i in range(1, n + 1):

                # A segment needs at least 2 points
                if i >= 2:
                    prefix = (prefix + dp[i - 1][j - 1]) % MOD

                # Either:
                # 1. Don't use point i-1
                # 2. End a new segment at i-1
                dp[i][j] = (dp[i - 1][j] + prefix) % MOD

        return dp[n][k]