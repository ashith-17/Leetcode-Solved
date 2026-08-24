class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        
        n = len(stones)

        # Convert stones into prefix sums
        for i in range(1, n):
            stones[i] = stones[i] + stones[i - 1]

        # If Alice takes all remaining stones on the final move,
        # the score difference is the total sum.
        best = stones[n - 1]

        # Work backwards.
        # We never use stones[0] as a stopping point because
        # the first move must take at least 2 stones.
        for i in range(n - 2, 0, -1):

            # Two choices:
            #
            # 1. Don't choose prefix i:
            #    keep the best result already calculated.
            #
            # 2. Choose prefix i:
            #    Alice gets stones[i],
            #    then Bob gets the advantage represented by best.
            #
            # So the resulting difference is stones[i] - best.
            best = max(best, stones[i] - best)

        return best