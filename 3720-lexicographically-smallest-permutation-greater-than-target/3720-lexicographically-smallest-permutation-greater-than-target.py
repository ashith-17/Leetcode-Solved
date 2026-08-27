class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters available in s
        freq = [0] * 26

        for ch in s:
            index = ord(ch) - ord('a')
            freq[index] += 1

        # Try to match target from left to right
        matched = 0

        while matched < n:

            index = ord(target[matched]) - ord('a')

            if freq[index] == 0:
                break

            freq[index] -= 1
            matched += 1

        # If we matched everything, target itself is not valid
        if matched == n:
            pos = n - 1
        else:
            # target[pos] could not be matched,
            # so we can try making THIS position larger.
            pos = matched

        while pos >= 0:

            # If this character was previously consumed,
            # put it back.
            if pos < matched:
                index = ord(target[pos]) - ord('a')
                freq[index] += 1

            current = ord(target[pos]) - ord('a')

            # Find the smallest available character
            # that is strictly greater than target[pos].
            greater = -1

            for j in range(current + 1, 26):

                if freq[j] > 0:
                    greater = j
                    break

            if greater != -1:

                # Prefix stays equal to target.
                answer = target[:pos]

                # Make this position larger.
                answer += chr(greater + ord('a'))

                # Use that character.
                freq[greater] -= 1

                # Fill the remaining positions with
                # the smallest available characters.
                for j in range(26):

                    while freq[j] > 0:
                        answer += chr(j + ord('a'))
                        freq[j] -= 1

                return answer

            # We cannot increase this position.
            # Go one position to the left.
            pos -= 1

        return ""