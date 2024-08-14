class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        left, right = 0, 0
        count = 0

        # While the right pointer hasn't reached the end of the string
        while right < len(s):
            # Move the right pointer to the end of the current group
            while right < len(s) and s[right] == s[left]:
                right += 1

            # The length of the current group
            current_group_length = right - left

            # Move the left pointer to the start of the next group
            left = right

            # Move the right pointer to the end of the next group
            while right < len(s) and s[right] == s[left]:
                right += 1

            # The length of the next group
            next_group_length = right - left

            # The number of valid substrings is the minimum of the two group lengths
            count += min(current_group_length, next_group_length)

            # Set the left pointer to the right pointer to continue to the next iteration
            left = right

        return count


        
