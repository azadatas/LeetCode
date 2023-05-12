import "strconv"

func isPalindrome(x int) bool {
	a := strconv.Itoa(x)
	b := []rune(a)
	for i := 0; i < len(a)/2; i++ {
		if b[i] != b[len(b)-1-i] {
			return false
		}
	}
	return true
}