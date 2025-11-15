class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        L, R = 0, len(height) - 1

        while L < R:
            curArea = min(height[L], height[R]) * (R - L)
            maxWater = max(maxWater, curArea)
            
            if height[L] > height[R]:
                R -= 1
            elif height[L] <= height[R]:
                L += 1

        return maxWater