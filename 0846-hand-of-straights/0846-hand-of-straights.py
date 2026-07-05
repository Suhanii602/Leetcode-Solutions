class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize:
            return False

        count = Counter(hand)

        for card in sorted(hand):
            if count[card] == 0:
                continue

            for x in range(card, card + groupSize):
                if count[x] == 0:
                    return False
                count[x] -= 1

        return True