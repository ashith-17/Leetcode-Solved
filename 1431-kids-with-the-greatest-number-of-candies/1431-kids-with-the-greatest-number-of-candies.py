class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n=len(candies)
        result=[False]*n
        largest=float('-inf')
        for i in range(n):
            if candies[i]>largest:
                largest=candies[i]
        for i in range(n):
            if (candies[i]+extraCandies)>= largest:
                result[i]=True
        return result
        