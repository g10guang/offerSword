package main

/**
 *
 * @param n int整型
 * @return int整型
 */
// https://www.nowcoder.com/practice/c6c7742f5ba7442aada113136ddea0c3?tpId=13&tqId=11160&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
func Fibonacci(n int) int {
	result := make([]int, n+1)
	result[1] = 1
	result[2] = 1
	for i := 3; i <= n; i++ {
		result[i] = result[i-1] + result[i-2]
	}
	return result[n]
}
