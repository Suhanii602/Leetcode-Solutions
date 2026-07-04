class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        cash = []

        for bill in bills:
            if bill == 5:
                cash.append(5)

            elif bill == 10:
                if 5 in cash:
                    cash.remove(5)
                    cash.append(10)
                else:
                    return False

            else:
                if 10 in cash and 5 in cash:
                    cash.remove(10)
                    cash.remove(5)
                elif cash.count(5) >= 3:
                    cash.remove(5)
                    cash.remove(5)
                    cash.remove(5)
                else:
                    return False

        return True