import math
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        distlist = []

        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]

            dist = x*x + y*y
            distlist.append([dist, points[i]])

        distlist.sort()

        ans = []
        for i in range(k):
            ans.append(distlist[i][1])

        return ans
