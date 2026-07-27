class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = 0
        second = 1
        if nums[1] > nums[0]:
          largest, second = 1, 0
        for i in range(2,len(nums)):
            if nums[i]>nums[largest]:
                second=largest
                largest=i
            elif nums[i]>nums[second]:
                second=i
        return (nums[largest]-1) * (nums[second]-1)