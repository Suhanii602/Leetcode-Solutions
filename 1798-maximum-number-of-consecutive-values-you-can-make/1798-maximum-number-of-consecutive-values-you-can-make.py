class Solution(object):
    def getMaximumConsecutive(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        coins.sort()
        base=1
        for i in coins:
            if i> base:
                break
            base+=i
        return base
