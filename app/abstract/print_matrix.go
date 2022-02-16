package main

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param matrix int整型二维数组
 * @return int整型一维数组
 */
// https://www.nowcoder.com/practice/9b4c81a02cd34f76be2659fa0d54342a?tpId=13&tqId=11172&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
func printMatrix(matrix [][]int) []int {
	lenr := len(matrix)
	if lenr == 0 {
		return nil
	}
	lenc := len(matrix[0])
	if lenc == 0 {
		return nil
	}
	result := make([]int, 0, lenr*lenc)
	minr := 0
	maxr := lenr - 1
	minc := 0
	maxc := lenc - 1
	for minr <= maxr && minc <= maxc {
		// 向右遍历
		for y := minc; y <= maxc; y++ {
			result = append(result, matrix[minr][y])
		}
		// 向下遍历
		for x := minr + 1; x <= maxr; x++ {
			result = append(result, matrix[x][maxc])
		}
		// 向左遍历
		for y := maxc - 1; y >= minc && minr != maxr; y-- {
			result = append(result, matrix[maxr][y])
		}
		// 向上遍历
		for x := maxr - 1; x > minr && minc != maxc; x-- {
			result = append(result, matrix[x][minc])
		}
		minr++
		maxr--
		minc++
		maxc--
	}
	return result
}
