class Solution(object):
    def resultArray(self, nums, k):
        result = [0] * k
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k

            new_dp[num % k] += 1

            for r in range(k):
                if dp[r]:
                    new_dp[(r * num) % k] += dp[r]

            dp = new_dp

            for r in range(k):
                result[r] += dp[r]

        return result
        