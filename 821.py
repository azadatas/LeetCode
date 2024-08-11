class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ind = []
        for i, ch in enumerate(s):
            if ch == c:
                ind.append(i)

        left, right = 0, 1

        answer = []
        for i, ch in enumerate(s):
            if right < len(ind) and i > ind[right]:
                left += 1
                right += 1

            if i <= ind[left]:
                answer.append(ind[left]-i)
            elif right < len(ind):
                ins = min(i-ind[left], ind[right]-i)
                answer.append(ins)
            else:
                answer.append(i - ind[left])
        
        return answer

        
