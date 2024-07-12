class Solution:
    def ispalindrome(self, word: str) -> bool:
        left = 0
        right = len(word) - 1
        while left < right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True
    
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.ispalindrome(word):
                return word
        return ""
