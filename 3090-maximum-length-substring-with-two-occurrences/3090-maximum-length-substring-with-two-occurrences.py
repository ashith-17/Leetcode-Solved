class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        freq = {}
        left = 0
        best = 0

        for right in range(len(s)):

            ch = s[right]
            freq[ch] = freq.get(ch, 0) + 1

            while freq[ch] > 2:
                left_char = s[left]
                freq[left_char] -= 1
                left += 1

            window = right - left + 1
            best = max(best, window)

        return best
        