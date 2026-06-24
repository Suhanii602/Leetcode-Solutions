class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones) > 1:
            stones.sort()

            if stones[-1] == stones[-2]:
                stones.pop()
                stones.pop()
            else:
                c = stones[-1] - stones[-2]
                stones.pop()
                stones.pop()
                stones.append(c)

        return stones[0] if stones else 0

