class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1
        max_amount = -1

        while l < r:
            curr_amount = (r - l) * min(heights[l] , heights[r])
            max_amount = max(max_amount, curr_amount)

            if heights[l] < heights[r]:
                l += 1
                
            else:
                r -= 1

        return max_amount
