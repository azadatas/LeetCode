class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        i, j = 0, 0
        distance_value = 0
        
        while i < len(arr1):
            while j < len(arr2) and arr2[j] < arr1[i] - d:
                j += 1
            if j == len(arr2) or arr2[j] > arr1[i] + d:
                distance_value += 1
            i += 1
        
        return distance_value

