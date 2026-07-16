class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        areaA = (ax2 - ax1) * (ay2 - ay1)
        areaB = (bx2 - bx1) * (by2 - by1)

        left = max(ax1, bx1)
        right = min(ax2, bx2)
        bottom = max(ay1, by1)
        top = min(ay2, by2)

        overlapWidth = max(0, right - left)
        overlapHeight = max(0, top - bottom)

        overlapArea = overlapWidth * overlapHeight

        return areaA + areaB - overlapArea