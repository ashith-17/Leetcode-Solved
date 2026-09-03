class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        
        min_odd = float('inf')

        # Find the smallest odd number
        for x in nums1:
            if x % 2 == 1:
                if x < min_odd:
                    min_odd = x

        # If there is no odd number,
        # all numbers are already even.
        if min_odd == float('inf'):
            return True

        # If an even number is smaller than the
        # smallest odd number, that even number
        # cannot be changed to odd.
        for x in nums1:
            if x % 2 == 0 and x < min_odd:
                return False

        return True