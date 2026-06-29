class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        diff = [0] * 1001      # locations are <= 1000

        for p, start, end in trips:
            diff[start] += p
            diff[end] -= p

        passengers = 0

        for change in diff:
            passengers += change
            if passengers > capacity:
                return False

        return True