func diagonalSum(mat [][]int) int {
	SumOfDiagonalElements := 0
	for i := 0; i < len(mat); i++ {
		SumOfDiagonalElements = SumOfDiagonalElements + mat[i][i] + mat[i][len(mat)-1-i]
	}
	if len(mat)%2 == 1 {
		SumOfDiagonalElements = SumOfDiagonalElements - mat[(len(mat)-1)/2][(len(mat)-1)/2]
	}
	return SumOfDiagonalElements
}