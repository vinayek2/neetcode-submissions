class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        max height and then find how many spaces away it is from the 
        '''
       
        maxArea = 0

        for i in range(len(heights)):
            left = heights[i]
            for j in range(len(heights)-1, 0, -1):
                right = heights[j]
                value = min(left, right) * (j - i)
                if(value > maxArea):
                    maxArea = value

            

        return maxArea
            

    