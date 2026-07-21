class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0

        for bit in range(32):

            count = 0
            for num in nums:

                if (num >> bit) & 1:
                    count += 1

            if count % 3:
                ans |= (1 << bit)

        # Handle negative numbers
        if ans >= 2**31:
            ans -= 2**32

        return ans