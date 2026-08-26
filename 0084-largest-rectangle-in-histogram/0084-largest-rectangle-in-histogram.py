class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i in range(len(heights) + 1):

            curr_height = 0 if i == len(heights) else heights[i]

            while stack and heights[stack[-1]] > curr_height:
                mid = stack.pop()

                height = heights[mid]

                left = stack[-1] if stack else -1
                right = i

                width = right - left - 1

                area = height * width

                max_area = max(max_area, area)

            stack.append(i)

        return max_area