class Solution:
    def trap(self, height: List[int]) -> int:
      stack = []
      water = 0

      for i in range(len(height)):

        while stack and height[i] > height[stack[-1]]:

            bottom = stack.pop()

            if not stack:
                break

            left = stack[-1]

            width = i - left - 1

            water_height = min(height[left], height[i]) - height[bottom]

            water += width * water_height

        stack.append(i)

      return water