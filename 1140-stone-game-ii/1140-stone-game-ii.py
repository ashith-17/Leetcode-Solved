from functools import cache
from itertools import accumulate

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # suffix[i] = sum of stones from i to end
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @cache
        def dfs(i, M):
            # No piles left
            if i >= n:
                return 0

            # Can take all remaining piles
            if i + 2 * M >= n:
                return suffix[i]

            best = 0

            for X in range(1, 2 * M + 1):
                best = max(
                    best,
                    suffix[i] - dfs(i + X, max(M, X))
                )

            return best

        return dfs(0, 1)