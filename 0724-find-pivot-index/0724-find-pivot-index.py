class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum=0
        rightsum=0
        total=0
        for i in range(len(nums)):
            total+=nums[i]
        for i in range(len(nums)):
            rightsum=total-leftsum-nums[i]
            if leftsum==rightsum:
                return i
            leftsum+=nums[i]
        return -1