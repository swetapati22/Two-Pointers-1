# Time Complexity :
- O(n^2), where n is the length of the array outer loop + two-pointer inner loop

# Space Complexity :
- O(1), ignoring the space for the output list no extra data structures used

# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplet = []
        nums.sort()
        
        for curr_idx in range(len(nums)):
            if curr_idx != 0 and nums[curr_idx] == nums[curr_idx - 1]:
                continue

            target = -nums[curr_idx]
            left = curr_idx + 1
            right = len(nums) - 1

            while left < right:
                two_sum = nums[left] + nums[right]
                if two_sum == target:
                    triplet.append([nums[curr_idx], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif two_sum < target:
                    left += 1
                else:
                    right -= 1

        return triplet


