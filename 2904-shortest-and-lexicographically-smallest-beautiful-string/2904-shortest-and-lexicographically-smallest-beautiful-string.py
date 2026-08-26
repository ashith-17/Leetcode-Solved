class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        
        left = 0
        ones = 0

        best = ""

        for right in range(len(s)):

            if s[right] == '1':
                ones += 1

            # Too many 1s -> remove from the left
            while ones > k:

                if s[left] == '1':
                    ones -= 1

                left += 1

            # We have exactly k ones.
            # Remove unnecessary leading zeroes.
            while ones == k and left < right and s[left] == '0':
                left += 1

            # Current window is beautiful
            if ones == k:

                candidate = s[left:right + 1]

                if best == "":
                    best = candidate

                elif len(candidate) < len(best):
                    best = candidate

                elif len(candidate) == len(best) and candidate < best:
                    best = candidate
        return best