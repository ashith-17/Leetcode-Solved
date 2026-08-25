class Solution:
  def sumSubarrayMins(self, arr: List[int]) -> int:
    MOD = 10**9 + 7
    n = len(arr)

    prev = [-1] * n
    next_ = [n] * n

    stack = []

    # Previous strictly smaller
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()

        if stack:
            prev[i] = stack[-1]

        stack.append(i)

    stack = []

    # Next smaller or equal
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()

        if stack:
            next_[i] = stack[-1]

        stack.append(i)

    ans = 0

    for i in range(n):
        left = i - prev[i]
        right = next_[i] - i

        ans += arr[i] * left * right

    return ans % MOD