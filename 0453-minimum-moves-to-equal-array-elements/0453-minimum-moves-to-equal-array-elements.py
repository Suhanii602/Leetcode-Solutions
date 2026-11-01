class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mn = min(nums)
        return sum(num - mn for num in nums)