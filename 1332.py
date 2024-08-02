class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if self.ispal(s):
            return 1
        else:
            return 2

    def ispal(self, s:str)-> bool:
        left, right = 0, len(s)-1
        while left < right:
            if s[left]!= s[right]:
                return False
            left += 1
            right -= 1
        return True
