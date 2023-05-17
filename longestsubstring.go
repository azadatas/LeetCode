func lengthOfLongestSubstring(s string) int {
	var ans, start int
	charMap := make(map[rune]int)

	for i, v := range s {
		if index, ok := charMap[v]; ok && index >= start {
			start = index + 1
		}
		charMap[v] = i
		if ans < i-start+1 {
			ans = i - start + 1
		}
	}

	return ans
}