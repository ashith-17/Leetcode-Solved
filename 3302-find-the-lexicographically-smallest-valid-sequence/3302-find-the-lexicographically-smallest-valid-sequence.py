class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)

        # suf[i] = smallest index in word2 that cannot be matched
        # using word1[i:]
        suf = [m] * (n + 1)

        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                j -= 1
            suf[i] = j + 1

        ans = []
        j = 0
        used = False

        for i in range(n):
            if j == m:
                break

            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            elif (
                not used
                and suf[i + 1] <= j + 1
            ):
                used = True
                ans.append(i)
                j += 1

        if j == m:
            return ans
        return []