class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        summ = n * (n + 1) // 2
        actualsum = sum(nums)
        return summ - actualsum