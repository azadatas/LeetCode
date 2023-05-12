import "strconv"

func isPalindrome(x int) bool {
	IntToString := strconv.Itoa(x)
	IntToRunes := []rune(IntToString)
	for i := 0; i < len(IntToRunes)/2; i++ {
		if IntToRunes[i] != IntToRunes[len(IntToRunes)-1-i] {
			return false
		}
	}
	return true
}