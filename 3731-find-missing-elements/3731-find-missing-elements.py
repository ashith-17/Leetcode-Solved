class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = set(nums)

        smallest = min(nums)
        largest = max(nums)

        ans = []

        for i in range(smallest + 1, largest):
            if i not in s:
                ans.append(i)

        return ans
