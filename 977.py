class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = [0] * len(nums)
        left, right = 0, len(nums)-1
        squ = len(nums)-1
        while left < right:
            if nums[left]*-1 > nums[right]:
                squares[squ] = nums[left] ** 2
                left += 1
                squ -= 1
            elif nums[left]*-1 < nums[right]:
                squares[squ] = nums[right] ** 2
                right -= 1
                squ -= 1
            else:
                squares[squ] = nums[right] ** 2
                squ -= 1
                squares[squ] = nums[right] ** 2
                squ -= 1
                left += 1
                right -= 1
        if left == right:
            squares[squ] = nums[left]**2
        return squares
            
