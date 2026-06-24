class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans=[]
        nums.sort(reverse=True)
        for i in range(k):
            ans.append(nums[i])
        return ans[-1]