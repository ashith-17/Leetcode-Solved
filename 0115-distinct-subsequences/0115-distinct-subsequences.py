class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp[j] = number of ways to form t[:j]
        # using the characters processed from s so far
        dp = [0] * (len(t) + 1)

        # There is exactly one way to form an empty string:
        # choose nothing.
        dp[0] = 1

        for i in range(len(s)):

            # Go backwards so dp[j-1] is still
            # from the previous iteration.
            for j in range(len(t), 0, -1):

                if s[i] == t[j - 1]:

                    # Two possibilities:
                    #
                    # 1. Use s[i]  -> dp[j-1]
                    # 2. Skip s[i] -> old dp[j]
                    #
                    dp[j] = dp[j] + dp[j - 1]

        return dp[len(t)]