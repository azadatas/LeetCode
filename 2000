class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i, char in enumerate(word):
            if char == ch:
                left = 0
                right = i
                copy = list(word[:i+1])
                while left < right:
                    copy[left], copy[right] = word[right], word[left]
                    left += 1
                    right -= 1
                result = ''.join(copy) + word[i+1:]
                return result  

        return word  
  
