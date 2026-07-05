class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''n=len(nums)
        target=n-1
        for i in range(n-1,-1,-1):
            maxjump=nums[i]
            if i+maxjump>=target:
                target=i
        return target==0'''
        maxreach=0
        for currpos, jump in enumerate(nums):
            if maxreach<currpos:
                return False
            maxreach=max(maxreach, currpos+jump)
        return True