class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        ans = []

        while True:
            choices = [(a, 'a'), (b, 'b'), (c, 'c')]
            choices.sort(reverse=True)

            placed = False

            for cnt, ch in choices:
                if cnt == 0:
                    continue

                if len(ans) >= 2 and ans[-1] == ans[-2] == ch:
                    continue

                ans.append(ch)

                if ch == 'a':
                    a -= 1
                elif ch == 'b':
                    b -= 1
                else:
                    c -= 1

                placed = True
                break

            if not placed:
                break

        return "".join(ans)