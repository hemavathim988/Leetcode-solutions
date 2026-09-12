class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        # Store:
        # [start, end, weight, original_index]
        arr = []

        for i in range(n):
            arr.append([
                intervals[i][0],
                intervals[i][1],
                intervals[i][2],
                i
            ])

        # Sort by ending point
        arr.sort(key=lambda x: x[1])

        # Store all ending points
        ends = [x[1] for x in arr]

        # dp[i][j]
        # Best result using first i intervals
        # and selecting exactly j intervals
        #
        # (weight, indices)
        dp = [[None] * 5 for _ in range(n + 1)]

        # Selecting 0 intervals always gives weight 0
        for i in range(n + 1):
            dp[i][0] = (0, ())

        for i in range(1, n + 1):

            start, end, weight, index = arr[i - 1]

            # Find last interval whose end < current start
            left = 0
            right = i - 2
            prev = -1

            while left <= right:

                mid = (left + right) // 2

                if ends[mid] < start:
                    prev = mid
                    left = mid + 1
                else:
                    right = mid - 1

            # We can select at most 4 intervals
            for j in range(1, 5):

                # Option 1: Skip current interval
                best = dp[i - 1][j]

                # Option 2: Take current interval
                previous = dp[prev + 1][j - 1]

                if previous is not None:

                    new_weight = previous[0] + weight

                    new_indices = tuple(
                        sorted(previous[1] + (index,))
                    )

                    candidate = (new_weight, new_indices)

                    if best is None:
                        best = candidate

                    elif candidate[0] > best[0]:
                        best = candidate

                    elif candidate[0] == best[0]:
                        if candidate[1] < best[1]:
                            best = candidate

                dp[i][j] = best

       
        answer = (0, ())

        for j in range(1, 5):

            if dp[n][j] is not None:

                if dp[n][j][0] > answer[0]:
                    answer = dp[n][j]

                elif dp[n][j][0] == answer[0]:

                    if dp[n][j][1] < answer[1]:
                        answer = dp[n][j]

        return list(answer[1])