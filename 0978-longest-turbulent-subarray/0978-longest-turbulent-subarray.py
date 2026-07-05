class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)

        if n == 1:
            return 1

        ans = 1
        curr = 1

        for i in range(1, n):
            if arr[i] == arr[i-1]:
                curr = 1
            elif i == 1 or (arr[i] > arr[i-1] and arr[i-1] < arr[i-2]) or \
                           (arr[i] < arr[i-1] and arr[i-1] > arr[i-2]):
                curr += 1
            else:
                curr = 2

            ans = max(ans, curr)

        return ans

        return ans
