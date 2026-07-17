class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        closestX=min(max(xCenter,x1),x2)
        closestY=min(max(yCenter,y1),y2)
        dx=xCenter-closestX
        dy=yCenter-closestY
        return dx*dx+dy*dy<=radius*radius