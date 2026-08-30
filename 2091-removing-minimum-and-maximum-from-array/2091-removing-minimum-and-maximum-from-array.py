class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        n = len(nums)

        min_index = 0
        max_index = 0

        # Find the indices of minimum and maximum
        for i in range(n):

            if nums[i] < nums[min_index]:
                min_index = i

            if nums[i] > nums[max_index]:
                max_index = i

        # Make sure min_index is the smaller index
        if min_index > max_index:
            min_index, max_index = max_index, min_index

        # Option 1:
        # Remove everything from the front
        front = max_index + 1

        # Option 2:
        # Remove everything from the back
        back = n - min_index

        # Option 3:
        # Remove min from front and max from back
        both_ends = (min_index + 1) + (n - max_index)

        return min(front, back, both_ends)