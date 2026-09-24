class Solution:
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            if sum(map(int, str(nums[i]))) == i:
                return i
        return -1