package main

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param A int整型一维数组
 * @return int整型一维数组
 */
// https://www.nowcoder.com/practice/94a4d381a68b47b7a8bed86f2975db46?tpId=13&tqId=11204&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
func multiply(A []int) []int {
	l := len(A)
	left := make([]int, l)
	right := make([]int, l)
	result := make([]int, l)
	if l == 0 {
		return result
	}
	left[0] = A[0]
	for i := 1; i < l; i++ {
		left[i] = left[i-1] * A[i]
	}
	right[l-1] = A[l-1]
	for j := l - 2; j >= 0; j-- {
		right[j] = right[j+1] * A[j]
	}
	for i := 0; i < l; i++ {
		leftPart := i - 1
		rightPart := i + 1
		n := 1
		if leftPart >= 0 {
			n = n * left[leftPart]
		}
		if rightPart < l {
			n = n * right[rightPart]
		}
		result[i] = n
	}
	return result
}
