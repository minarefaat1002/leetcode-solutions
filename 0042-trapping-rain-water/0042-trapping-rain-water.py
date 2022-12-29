class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = height[0]
        maxRight = height[-1]
        water = 0
        l = 1
        r = len(height)-2
        while l <= r:
            if maxLeft <= maxRight:
                curHeight = height[l]
                water += max(min(maxLeft,maxRight)-curHeight,0)
                maxLeft = max(maxLeft,curHeight)
                l+=1
            else:
                curHeight = height[r]
                water += max(min(maxLeft,maxRight)-curHeight,0)
                maxRight = max(maxRight,curHeight)
                r-=1
        return water 
    
                
            