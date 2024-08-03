class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left]* -1 == nums[right]:
                return nums[right]
            elif nums[left]* -1 > nums[right]:
                left += 1
            else:
                right -= 1
        return -1
