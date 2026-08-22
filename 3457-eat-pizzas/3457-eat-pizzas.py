class Solution(object):
    def maxWeight(self, pizzas):
        """
        :type pizzas: List[int]
        :rtype: int
        """
        pizzas.sort()

        k = len(pizzas) // 4
        odd = (k + 1) // 2
        even = k // 2

        stack = []

        # Odd days: take the largest pizza
        for _ in range(odd):
            stack.append(pizzas[-1])
            pizzas.pop()

        # Even days: use two largest pizzas,
        # gain the smaller one
        for _ in range(even):
            stack.append(pizzas[-2])
            pizzas.pop()
            pizzas.pop()

        return sum(stack)