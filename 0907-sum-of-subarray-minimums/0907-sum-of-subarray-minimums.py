class Solution:
 def sumSubarrayMins(self, arr: List[int]) -> int:
    MOD = 10**9 + 7
    stack = []
    ans = 0

    for i in range(len(arr)):
        while stack and arr[stack[-1]] > arr[i]:

            mid = stack.pop()

            left = stack[-1] if stack else -1
            right = i

            left_count = mid - left
            right_count = right - mid

            ans += arr[mid] * left_count * right_count

        stack.append(i)

    # Process remaining elements
    n = len(arr)

    while stack:
        mid = stack.pop()

        left = stack[-1] if stack else -1
        right = n

        left_count = mid - left
        right_count = right - mid

        ans += arr[mid] * left_count * right_count

    return ans % MOD