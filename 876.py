class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new = []
        l, r = 0, 0
        n, m = len(word1), len(word2)

        while l<n and r<m:
            new.append(word1[l])
            new.append(word2[r])
            l += 1
            r += 1
            print(l,r)

        new.append(word1[l:])
        new.append(word2[r:])
        new = ''.join(new)
        return new
        
