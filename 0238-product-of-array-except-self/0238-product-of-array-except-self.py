class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)      # Example-nums=[1,2,3,4]
        answer=[1]*n     # answer=[1,1,1,1]
        prefix=1         # Prefix = product of all elements to the LEFT of the current index.
        for i in range(n):
            answer[i]=prefix  # answer=[1,1,2,6]
            prefix*=nums[i]   #prefix=1,2,6
        suffix=1
        for i in range(n-1,-1,-1):   # Suffix = product of all elements to the RIGHT of the current index.
            answer[i]*=suffix        # answer=[24,12,8,6]
            suffix*=nums[i]          # suffix=1,4,12,24
        return answer