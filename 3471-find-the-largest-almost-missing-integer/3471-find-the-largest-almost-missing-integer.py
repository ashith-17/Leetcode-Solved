class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        # Case 1:
        # The entire array is one window.
        if k == n:
            return max(nums)

        # Count frequency of every number.
        freq = {}

        for num in nums:

            if num not in freq:
                freq[num] = 0

            freq[num] += 1

        # Case 2:
        # Every element is its own window.
        if k == 1:

            answer = -1

            for num in nums:

                if freq[num] == 1:

                    if num > answer:
                        answer = num

            return answer

        # Case 3:
        # 1 < k < n
        #
        # Only nums[0] and nums[n-1]
        # can possibly be almost missing.

        answer = -1

        if freq[nums[0]] == 1:
            answer = nums[0]

        if freq[nums[n - 1]] == 1:

            if nums[n - 1] > answer:
                answer = nums[n - 1]

        return answer