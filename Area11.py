class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        l, r =  0, len(height) - 1
        maxArea = 0 
        

        while l < r:

            #area = width(r - l) * min height of each height
            width = r - l
            minHeight = min(height[l], height[r])
            area = width * minHeight

            #obtain the max area by comparing new max and old max
            maxArea = max(maxArea, area)

            #if left height is smaller than the right height increment it
            if height[l] < height[r]:
                l += 1
            #else right height is greater than or equal to it so dec it
            else:
                r -= 1
        
        return maxArea
