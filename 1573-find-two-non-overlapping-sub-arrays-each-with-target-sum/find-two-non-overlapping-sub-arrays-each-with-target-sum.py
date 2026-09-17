class Solution(object):
    def minSumOfLengths(self, arr, target):
        n = len(arr)

        # best[i] = minimum length of a valid subarray
        # completely inside arr[0:i]
        best = [float('inf')] * (n + 1)

        left = 0
        total = 0
        ans = float('inf')

        for right in range(n):
            total += arr[right]

            while total > target:
                total -= arr[left]
                left += 1

            if total == target:
                length = right - left + 1

                # Combine current subarray with the best
                # non-overlapping subarray before it
                if best[left] != float('inf'):
                    ans = min(ans, length + best[left])

                # Update best valid subarray
                best[right + 1] = min(best[right], length)
            else:
                best[right + 1] = best[right]

        return -1 if ans == float('inf') else ans