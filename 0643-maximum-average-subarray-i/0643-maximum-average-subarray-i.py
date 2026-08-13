class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = 0

        # Calculate sum of the first window
        for i in range(k):
            window_sum += nums[i]

        max_sum = window_sum

        # Slide the window
        for i in range(k, len(nums)):
            window_sum += nums[i]
            window_sum -= nums[i - k]

            if window_sum > max_sum:
                max_sum = window_sum

        return max_sum / k

