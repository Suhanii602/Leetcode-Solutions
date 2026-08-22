class Solution(object):
    def maximumNumber(self, num, change):
        """
        :type num: str
        :type change: List[int]
        :rtype: str
        """
        num=list(num)
        start=False
        for i in range(len(num)):
            digit=int(num[i])
            if change[digit]> digit:
                num[i] =str(change[digit])
                start=True
            elif change[digit]==digit:
                if start:
                    num[i] =str(change[digit])
            else:
                if start:
                    break
        return ''.join(num)