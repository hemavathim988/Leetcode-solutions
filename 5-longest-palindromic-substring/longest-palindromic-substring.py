class Solution:
    def longestPalindrome(self, s):

        if len(s) < 2:
            return s

        start = 0
        max_len = 1

        for i in range(len(s)):

            
            left = i
            right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    max_len = right - left + 1
                    start = left

                left -= 1
                right += 1

            
            left = i
            right = i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    max_len = right - left + 1
                    start = left

                left -= 1
                right += 1

        return s[start:start + max_len]