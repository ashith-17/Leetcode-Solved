class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        
        n = len(stoneValue)

        # Prefix sum
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        # memo[l][r] = maximum score Alice can get
        # from stoneValue[l...r]
        memo = [[None] * n for _ in range(n)]

        def dfs(l, r):

            # Only one stone remains
            if l == r:
                return 0

            # Already calculated
            if memo[l][r] is not None:
                return memo[l][r]

            answer = 0

            # Initially the whole interval is on the right
            left_sum = 0
            right_sum = prefix[r + 1] - prefix[l]

            # Try every split
            for k in range(l, r):

                # Move stoneValue[k] from right side to left side
                left_sum += stoneValue[k]
                right_sum -= stoneValue[k]

                # Left side is smaller
                if left_sum < right_sum:

                    # Maximum possible score from this choice
                    # cannot exceed 2 * left_sum.
                    #
                    # If we already have this much,
                    # this split cannot improve answer.
                    if answer >= 2 * left_sum:
                        continue

                    score = left_sum + dfs(l, k)

                    if score > answer:
                        answer = score

                # Right side is smaller
                elif left_sum > right_sum:

                    # Maximum possible score from this choice
                    # cannot exceed 2 * right_sum.
                    #
                    # right_sum keeps decreasing as k moves right.
                    # Therefore all later choices are also useless.
                    if answer >= 2 * right_sum:
                        break

                    score = right_sum + dfs(k + 1, r)

                    if score > answer:
                        answer = score

                # Both sides are equal
                else:

                    left_score = left_sum + dfs(l, k)

                    right_score = right_sum + dfs(k + 1, r)

                    if left_score > answer:
                        answer = left_score

                    if right_score > answer:
                        answer = right_score

            memo[l][r] = answer

            return answer

        return dfs(0, n - 1)