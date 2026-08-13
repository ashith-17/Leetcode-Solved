class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        new=[0]*(len(gain)+1)
        for i in range(len(gain)):
            new[i+1]=gain[i]+new[i]
        return max(new)