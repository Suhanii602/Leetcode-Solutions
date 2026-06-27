class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        sortlist= sorted(freq.items(), key=lambda x:x[1], reverse=True)
        return [sortlist[i][0] for i in range(k)]