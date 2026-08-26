class Solution:
 def subArrayRanges(self, nums: List[int]) -> int:
    n = len(nums)

    # ---------- Sum of subarray minimums ----------
    min_sum = 0
    stack = []

    for i in range(n + 1):
        while stack and (
            i == n or nums[stack[-1]] > nums[i]
        ):
            mid = stack.pop()

            left = stack[-1] if stack else -1
            right = i

            left_count = mid - left
            right_count = right - mid

            min_sum += nums[mid] * left_count * right_count

        if i < n:
            stack.append(i)

    # ---------- Sum of subarray maximums ----------
    max_sum = 0
    stack = []

    for i in range(n + 1):
        while stack and (
            i == n or nums[stack[-1]] < nums[i]
        ):
            mid = stack.pop()

            left = stack[-1] if stack else -1
            right = i

            left_count = mid - left
            right_count = right - mid

            max_sum += nums[mid] * left_count * right_count

        if i < n:
            stack.append(i)

    return max_sum - min_sum