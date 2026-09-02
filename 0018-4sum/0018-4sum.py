class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)

        nums.sort()

        answer = []

        for i in range(n - 3):

            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Smallest possible sum using this i
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break

            # Largest possible sum using this i
            if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
                continue

            for j in range(i + 1, n - 2):

                # Skip duplicate second elements
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Smallest possible sum using i and j
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break

                # Largest possible sum using i and j
                if nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target:
                    continue

                left = j + 1
                right = n - 1

                while left < right:

                    total = (
                        nums[i]
                        + nums[j]
                        + nums[left]
                        + nums[right]
                    )

                    if total == target:

                        answer.append([
                            nums[i],
                            nums[j],
                            nums[left],
                            nums[right]
                        ])

                        # Skip duplicate third element
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1

                        # Skip duplicate fourth element
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1

                    elif total < target:
                        left += 1

                    else:
                        right -= 1

        return answer