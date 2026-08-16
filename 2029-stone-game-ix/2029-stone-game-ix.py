class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        count0 = 0
        count1 = 0
        count2 = 0

        for stone in stones:
            remainder = stone % 3

            if remainder == 0:
                count0 += 1
            elif remainder == 1:
                count1 += 1
            else:
                count2 += 1

        if count0 % 2 == 0:
            return count1 > 0 and count2 > 0

        return abs(count1 - count2) > 2