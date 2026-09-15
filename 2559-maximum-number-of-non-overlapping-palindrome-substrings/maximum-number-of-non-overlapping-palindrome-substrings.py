class Solution(object):
    def maxPalindromes(self, s, k):
        n = len(s)

        # pal[i][j] = 1 if s[i:j+1] is a palindrome
        pal = [bytearray(n) for _ in range(n)]

        count = 0
        next_start = 0

        # Consider every possible ending position
        for end in range(n):

            # Check possible starting positions backwards
            for start in range(end, next_start - 1, -1):

                # Check whether s[start:end+1] is a palindrome
                if s[start] == s[end]:
                    length = end - start + 1

                    if length <= 2 or pal[start + 1][end - 1]:
                        pal[start][end] = 1

                        # We found a valid palindrome
                        if length >= k:
                            count += 1

                            # Next palindrome must start after this one
                            next_start = end + 1
                            break

        return count