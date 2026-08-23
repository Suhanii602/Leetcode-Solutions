class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        def rob_line(arr):

            if len(arr) == 1:
                return arr[0]

            best = [0] * len(arr)

            best[0] = arr[0]
            best[1] = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                best[i] = max(
                    best[i - 1],
                    arr[i] + best[i - 2]
                )

            return best[-1]

        option1 = rob_line(nums[:-1])
        option2 = rob_line(nums[1:])

        return max(option1, option2)