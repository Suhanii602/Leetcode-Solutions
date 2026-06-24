from collections import Counter
class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = Counter(s)

        maxFreq = max(freq.values())
        if maxFreq>(len(s) + 1)// 2:
            return ""

        chars =sorted(freq.keys(), key=lambda c: freq[c], reverse=True)

        res = [""] * len(s)
        idx = 0

        for ch in chars:
            for _ in range(freq[ch]):
                res[idx] = ch
                idx += 2

                if idx >= len(s):
                    idx = 1

        return "".join(res)        