class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        heights = [0] * cols
        max_area = 0

        for i in range(rows):

            for j in range(cols):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            stack = []

            for j in range(cols + 1):

                curr_height = 0 if j == cols else heights[j]

                while stack and heights[stack[-1]] > curr_height:
                    mid = stack.pop()

                    height = heights[mid]

                    left = stack[-1] if stack else -1
                    right = j

                    width = right - left - 1

                    area = height * width

                    max_area = max(max_area, area)

                if j < cols:
                    stack.append(j)

        return max_area