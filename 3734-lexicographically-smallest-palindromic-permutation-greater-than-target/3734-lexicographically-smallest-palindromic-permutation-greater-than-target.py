class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # -----------------------------------------
        # 1. Count every character in s
        # -----------------------------------------
        count = [0] * 26

        for ch in s:
            index = ord(ch) - ord('a')
            count[index] += 1

        # -----------------------------------------
        # 2. Check whether a palindrome is possible
        # -----------------------------------------
        middle = -1
        odd_count = 0

        for i in range(26):

            if count[i] % 2 == 1:
                odd_count += 1
                middle = i

        # More than one odd-frequency character
        # means no palindrome can be formed.
        if odd_count > 1:
            return ""

        # Remove the middle character.
        # Everything else must occur in pairs.
        if middle != -1:
            count[middle] -= 1

        # -----------------------------------------
        # 3. count[i] now represents characters
        #    available for BOTH halves.
        #
        #    We need count[i] / 2 copies in the
        #    left half.
        # -----------------------------------------

        half = [0] * 26

        for i in range(26):
            half[i] = count[i] // 2

        half_length = n // 2

        # -----------------------------------------
        # 4. Try to make the left half equal to
        #    target's left half.
        # -----------------------------------------
        remaining = half[:]

        matched = 0

        while matched < half_length:

            index = ord(target[matched]) - ord('a')

            if remaining[index] == 0:
                break

            remaining[index] -= 1
            matched += 1

        # -----------------------------------------
        # 5. If we can make the entire target left
        #    half, check whether the resulting
        #    palindrome is already > target.
        # -----------------------------------------
        if matched == half_length:

            left_part = target[:half_length]

            # Build the right half by reversing left.
            right_part = ""

            for i in range(half_length - 1, -1, -1):
                right_part += left_part[i]

            # Add middle character if n is odd.
            middle_part = ""

            if middle != -1:
                middle_part = chr(middle + ord('a'))

            candidate = left_part + middle_part + right_part

            if candidate > target:
                return candidate

        # -----------------------------------------
        # 6. We either could not match target fully,
        #    or matching it produced a palindrome
        #    that is <= target.
        #
        #    Now move backward and try to make one
        #    position larger.
        # -----------------------------------------

        # Start with the characters remaining after
        # matching as much of target as possible.
        remaining = half[:]

        for i in range(matched):
            index = ord(target[i]) - ord('a')
            remaining[index] -= 1

        # If target's whole left half was matched,
        # start by changing its last position.
        if matched == half_length:
            position = half_length - 1
        else:
            position = matched

        while position >= 0:

            # -------------------------------------
            # If this position was previously matched,
            # return its character to the pool.
            # -------------------------------------
            if position < matched:

                index = ord(target[position]) - ord('a')
                remaining[index] += 1

            current = ord(target[position]) - ord('a')

            # -------------------------------------
            # Find the smallest available character
            # strictly larger than target[position].
            # -------------------------------------
            greater = -1

            for j in range(current + 1, 26):

                if remaining[j] > 0:

                    greater = j
                    break

            if greater != -1:

                # ---------------------------------
                # Build the left half.
                # Prefix before position stays
                # exactly equal to target.
                # ---------------------------------
                answer = target[:position]

                # Make this position slightly larger.
                answer += chr(greater + ord('a'))

                # Use one pair of this character.
                remaining[greater] -= 1

                # ---------------------------------
                # Fill the rest of the left half
                # with the smallest available chars.
                # ---------------------------------
                for j in range(26):

                    while remaining[j] > 0:
                        answer += chr(j + ord('a'))
                        remaining[j] -= 1

                # ---------------------------------
                # Construct the right half by mirror.
                # ---------------------------------
                right = ""

                for i in range(len(answer) - 1, -1, -1):
                    right += answer[i]

                middle_part = ""

                if middle != -1:
                    middle_part = chr(middle + ord('a'))

                return answer + middle_part + right

            # This position cannot be increased.
            # Try an earlier position.
            position -= 1

        # No valid palindrome greater than target.
        return ""