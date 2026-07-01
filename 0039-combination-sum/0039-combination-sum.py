class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        curr = []

        def backtrack(start, target):
            if target == 0:
                ans.append(curr[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue

                curr.append(candidates[i])
                backtrack(i, target - candidates[i])  # reuse same number
                curr.pop()

        backtrack(0, target)
        return ans