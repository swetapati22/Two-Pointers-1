# Time Complexity :
- O(n), where n is the length of the height array single pass with two pointers

# Space Complexity :
- O(1), constant space used

# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            width = right - left
            min_height = min(height[left], height[right])
            max_water = max(max_water, width * min_height)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
