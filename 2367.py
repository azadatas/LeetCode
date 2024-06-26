class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        my_set = set(nums)
        count=0
        for num in my_set:
            if (num + diff) in my_set and (num + 2*diff) in my_set:
                count+=1
        return count



