class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s)-1
        while left < right:
            if s[left] >='a' and s[left]<='z' or s[left] >='A' and s[left]<='Z':
                if s[right] >='a' and s[right]<='z' or s[right] >='A' and s[right]<='Z':
                    s[left], s[right] = s[right], s[left]
                    left += 1
                    right -= 1
                else:
                    right -= 1
            else:
                left += 1
        
        return ''.join(s)
