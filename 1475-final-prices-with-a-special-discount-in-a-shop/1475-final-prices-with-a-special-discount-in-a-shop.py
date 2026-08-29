class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        n = len(prices)

        answer = prices.copy()
        stack = []

        for i in range(n):

            while stack and prices[stack[-1]] >= prices[i]:

                j = stack.pop()

                answer[j] = prices[j] - prices[i]

            stack.append(i)

        return answer