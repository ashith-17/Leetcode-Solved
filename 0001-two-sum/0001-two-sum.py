class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_maps={}
        for i,num in enumerate(nums):
            complement = target - num 
            if complement in num_maps:
                return[num_maps[complement],i]
            num_maps[num]=i