class Solution:
    def distinctSubseqII(self, s: str) -> int:

        MOD = 10**9 + 7

        dp = [0] * 26

        total = 0

        for ch in s:

            i = ord(ch) - ord('a')

            # Every existing distinct subsequence can be
            # extended by ch.
            new = (total + 1) % MOD

            # Replace the old subsequences ending in ch.
            total = (total - dp[i] + new) % MOD

            dp[i] = new

        return total