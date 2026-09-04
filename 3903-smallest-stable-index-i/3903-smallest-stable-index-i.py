class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        min_instability=[]
        instability=0
        pre=0
        suf=0
        answer=-1
        for i in range(0,n):
            pre=max(nums[0:i+1])
            suf=min(nums[i:n])
            instability=pre-suf
            if instability<=k:
                min_instability.append(i)
                answer=min(min_instability)
        return answer

                