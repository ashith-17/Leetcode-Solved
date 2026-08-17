class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        first = None
        second = None
        third = None

        for num in nums:

            # Ignore duplicate values
            if num == first or num == second or num == third:
                continue

            # num becomes the largest
            if first is None or num > first:
                third = second
                second = first
                first = num

            # num becomes the second largest
            elif second is None or num > second:
                third = second
                second = num

            # num becomes the third largest
            elif third is None or num > third:
                third = num

        # If third distinct maximum exists
        if third is not None:
            return third

        # Otherwise return maximum
        return first