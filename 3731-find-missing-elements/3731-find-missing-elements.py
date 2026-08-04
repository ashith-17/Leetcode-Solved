class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        smallest=min(nums)
        largest=max(nums)
        new=[]
        for i in range(smallest,largest):
            if i not in nums:
                new.append(i)
        return new
